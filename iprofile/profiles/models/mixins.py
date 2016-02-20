# -*- coding: utf-8 -*-

from IPython.core.profiledir import ProfileDir
from IPython.core.profileapp import ProfileCreate
from iprofile.utils.mixins import OSMixin


class IPythonProfileMixin(OSMixin):

    def check_startup_files(self):
        files = ['00_config.ipy', '01_scripts.py', ]
        for filename in files:
            self.new_file(
                self.join(self.settings.dirname, 'startup', filename)
            )


class IProfileDir(ProfileDir, IPythonProfileMixin):

    empty_def = lambda self: None
    ProfileDir.check_security_dir = empty_def
    ProfileDir.check_pid_dir = empty_def
    settings = None
    settings_file = u''

    @classmethod
    def find_profile_dir(cls, settings, *args, **kwargs):
        profile_dir = super(IProfileDir, cls).find_profile_dir(
            settings.dirname, *args, **kwargs)
        profile_dir.settings_file = settings.path
        profile_dir.settings = settings
        profile_dir.check_settings_file()
        profile_dir.check_startup_files()
        return profile_dir

    def check_settings_file(self):
        if self.settings and not self.settings.exists():
            self.settings.read()

    def check_dirs(self):
        super(IProfileDir, self).check_dirs()
        if self.settings:
            self.check_settings_file()
            self.check_startup_files()


class IProfileCreate(ProfileCreate, IPythonProfileMixin):

    def initialize(self, settings):
        self.settings = settings
        super(IProfileCreate, self).initialize()
        self.check_startup_files()
