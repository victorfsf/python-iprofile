# -*- coding: utf-8 -*-

from IPython.core.profiledir import ProfileDir
from iprofile.utils.mixins import OSMixin


class IProfileDir(ProfileDir, OSMixin):

    settings_file = u''

    @classmethod
    def find_profile_dir(self, path, settings, *args, **kwargs):
        self.settings = settings
        self.settings_file = path
        return super(IProfileDir, self).find_profile_dir(path, *args, **kwargs)

    def check_settings_file(self):
        if self.settings and not self.settings.exists:
            self.settings.read()
