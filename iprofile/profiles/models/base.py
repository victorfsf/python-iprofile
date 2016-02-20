# -*- coding: utf-8 -*-

from iprofile.utils.mixins import OSMixin
from iprofile.settings.models import ProfileSettings
from iprofile.settings.registry import settings
from iprofile.settings.utils import PROFILE_SETTINGS_FILE
from iprofile.profiles.models.mixins import IProfileDir
from iprofile.profiles.models.mixins import IProfileCreate
from IPython.core.profiledir import ProfileDirError
from slugify import slugify


class Profile(OSMixin):
    settings = None

    def __init__(self, name, *args, **kwargs):
        settings.read()
        if not settings.exists():
            raise Exception
        self.name = slugify(name)
        self.__path = self.absjoin(settings.get('profiles').get('path'), name)
        self.settings_file = self.join(self.__path, PROFILE_SETTINGS_FILE)
        if self.exists():
            self.load()

    def load(self):
        self.settings = ProfileSettings(self.settings_file)
        return self.settings

    def create(self):
        profile = IProfileCreate()
        profile.parse_command_line([
            '--profile-dir', self.__path
        ])
        profile.initialize(self.load())

    def locate(self):
        try:
            if self.settings:
                if not hasattr(self, '_iprofiledir'):
                    self._iprofiledir = IProfileDir.find_profile_dir(
                        self.__path, self.settings)
                return self._iprofiledir
            return self.__path if self.isfile(self.settings_file) else None
        except ProfileDirError:
            return

    def exists(self):
        return True if self.locate() else False

    def activate(self):
        if self.exists():
            settings.get('profiles').update({
                'active': self.name
            }).save()

    def deactivate(self):
        settings.get('profiles').update({
            'active': None
        }).save()

    def delete(self):
        self.remove(self.__path)
        self.settings = None

        active = settings.get('profiles').get('active')
        if self.name == active:
            self.deactivate()

        if hasattr(self, '_iprofiledir'):
            delattr(self, '_iprofiledir')
