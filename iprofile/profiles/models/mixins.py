# -*- coding: utf-8 -*-

from IPython.core.profiledir import ProfileDir
from IPython.core.profileapp import ProfileCreate
from iprofile.utils.mixins import OSMixin


class IPythonProfileMixin(OSMixin):

    def exclude_files(self):
        files = [
            'pid', 'security', 'log'
        ]
        for filename in files:
            self.remove(self.join(self.settings.dirname, filename))

    def create_files(self):
        files = [
            '00_config.ipy', '01_scripts.py'
        ]
        for filename in files:
            self.new_file(
                self.join(self.settings.dirname, 'startup', filename)
            )


class IProfileDir(ProfileDir, IPythonProfileMixin):

    settings_file = u''

    @classmethod
    def find_profile_dir(cls, path, settings, *args, **kwargs):
        profile_dir = super(IProfileDir, cls).find_profile_dir(
            path, *args, **kwargs)
        profile_dir.settings_file = path
        profile_dir.settings = settings
        if settings:
            profile_dir.exclude_files()
        return profile_dir

    def check_settings_file(self):
        if self.settings and not self.settings.exists:
            self.settings.read()


class IProfileCreate(ProfileCreate, IPythonProfileMixin):

    def initialize(self, settings):
        self.settings = settings
        super(IProfileCreate, self).initialize()
        self.exclude_files()
        self.create_files()
