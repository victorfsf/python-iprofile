# -*- coding: utf-8 -*-

from iprofile.settings.models.mixins import SettingsBase
from iprofile.settings.utils import GLOBAL_SETTINGS_FILE
from iprofile.settings.utils import PROFILE_SETTINGS_FILE


class GlobalSettings(SettingsBase):
    base_section = 'profiles'
    default = {
        base_section: {
            'path': 'iprofiles',
            'active': None
        }
    }

    def __init__(self, *args, **kwargs):
        super(SettingsBase, self).__init__(
            GLOBAL_SETTINGS_FILE, *args, **kwargs)


class ProfileSettings(SettingsBase):
    base_section = 'settings'
    default = {
        base_section: None
    }

    def __init__(self, global_settings, profile, *args, **kwargs):
        self._global = global_settings
        filepath = self.join(
            self._global.get('profiles').get('path'),
            profile,
            PROFILE_SETTINGS_FILE
        )
        super(SettingsBase, self).__init__(filepath, *args, **kwargs)
