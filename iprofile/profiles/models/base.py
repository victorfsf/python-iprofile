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
        self.dirname = self.absjoin(settings.get('profiles').get('path'), name)
        self.settings_file = self.join(self.dirname, PROFILE_SETTINGS_FILE)
        self.load()

    def load(self):
        if not self.isdir(self.dirname):
            return
        if not self.settings:
            self.settings = ProfileSettings(self.settings_file)
        return self.settings

    def create(self):
        profile = IProfileCreate()
        profile.parse_command_line([
            '--profile-dir', self.dirname
        ])
        self.makedirs(self.dirname)
        profile.initialize(self.load())

    def locate(self):

        if not self.load():
            self.delete()
            return

        if not hasattr(self, '_iprofiledir'):
            try:
                self._iprofiledir = IProfileDir.find_profile_dir(
                    self.settings)
            except ProfileDirError:
                return
        return self._iprofiledir

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
        self.remove(self.dirname)
        self.settings = None

        active = settings.get('profiles').get('active')
        if self.name == active:
            self.deactivate()

        if hasattr(self, '_iprofiledir'):
            delattr(self, '_iprofiledir')
