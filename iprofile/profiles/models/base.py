# -*- coding: utf-8 -*-

from iprofile.utils.mixins import OSMixin
from iprofile.settings.models import ProfileSettings
from iprofile.settings.registry import settings
from iprofile.settings.utils import PROFILE_SETTINGS_FILE
from IPython.core.profileapp import ProfileCreate
from iprofile.profiles.models.mixins import IProfileDir
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

    def create(self):
        profile = ProfileCreate()
        profile.parse_command_line([
            '--profile-dir', self.__path
        ])
        profile.initialize()
        self.load()

    def locate(self):
        try:
            return IProfileDir.find_profile_dir(self.__path, self.settings)
        except ProfileDirError:
            return

    def exists(self):
        return True if self.locate() else False
