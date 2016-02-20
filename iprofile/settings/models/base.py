# -*- coding: utf-8 -*-

from iprofile.settings.models.mixins import YAMLOrderedDict
from iprofile.settings.utils import GLOBAL_SETTINGS_FILE


class GlobalSettings(YAMLOrderedDict):
    default = {
        'path': 'iprofiles',
        'active': None
    }

    def __init__(self, *args, **kwargs):
        super(GlobalSettings, self).__init__(
            GLOBAL_SETTINGS_FILE, *args, **kwargs)
