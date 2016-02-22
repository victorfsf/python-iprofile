# -*- coding: utf-8 -*-

from IPython.core.profiledir import ProfileDir
from IPython.core.profileapp import ProfileCreate
from iprofile.utils.mixins import OSMixin
import sys


class IPythonProfileMixin(OSMixin):

    def check_startup_files(self):
        files = ['00_config.ipy', '01_scripts.py', ]
        for filename in files:
            self.new_file(
                self.join(self.path, 'startup', filename)
            )


class IProfileDir(ProfileDir, IPythonProfileMixin):

    empty_def = lambda self: None
    ProfileDir.check_security_dir = empty_def
    ProfileDir.check_pid_dir = empty_def
    ProfileDir.check_log_dir = empty_def
    path = None

    @classmethod
    def find_profile_dir(cls, path, *args, **kwargs):
        profile_dir = super(IProfileDir, cls).find_profile_dir(
            path, *args, **kwargs)
        profile_dir.path = path
        profile_dir.check_startup_files()
        return profile_dir

    def check_dirs(self):
        super(IProfileDir, self).check_dirs()
        if self.path:
            self.check_startup_files()


class IProfileCreate(ProfileCreate, IPythonProfileMixin):

    def initialize(self, argv=None):
        sys.argv = sys.argv[:3]
        self.parse_command_line([
            '--profile-dir', self.path
        ])
        super(IProfileCreate, self).initialize()
        self.check_startup_files()
