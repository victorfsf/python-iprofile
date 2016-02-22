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
