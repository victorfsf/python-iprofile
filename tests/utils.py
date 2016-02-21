# -*- coding: utf-8 -*-

from iprofile.settings.registry import settings
from iprofile.profiles.models import IProfileCreate
import os
import shutil


IProfileCreate.exit = lambda x, y: None


def set_up():
    settings.read(ignore_errors=True)
    try:
        os.makedirs(settings.get('path'))
    except OSError:
        pass


def tear_down():
    shutil.rmtree(settings.get('path'), ignore_errors=True)
    try:
        os.remove('iprofile.yml')
    except OSError:
        pass
