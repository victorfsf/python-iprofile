# -*- coding: utf-8 -*-

from iprofile.settings.models.mixins import YAMLOrderedDict
from iprofile.settings.utils import SETTINGS_FILE


class Settings(YAMLOrderedDict):
    default = {
        'path': 'iprofiles',
        'active': None
    }

    def __init__(self, *args, **kwargs):
        super(Settings, self).__init__(
            SETTINGS_FILE, *args, **kwargs)

    def get_path(self, value):
        return self.absuser(value)

    def get_append(self, value):
        return value if isinstance(value, dict) else {}
