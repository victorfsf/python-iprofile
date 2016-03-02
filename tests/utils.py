# -*- coding: utf-8 -*-

from iprofile.settings.registry import settings
from iprofile.profiles.models import IProfileCreate
import os
import shutil


IProfileCreate.exit = lambda x, y: None


def set_up():
    if os.path.isfile('iprofile.yml'):
        os.remove('iprofile.yml')
    settings.read(ignore_errors=True)
    settings.update({
        'pathlist': ['pathlist_test']
    }).save()
    try:
        os.makedirs(settings.get('path', 'iprofiles'))
    except OSError:
        pass


def tear_down():
    shutil.rmtree(settings.get('path', 'iprofiles'), ignore_errors=True)
    shutil.rmtree('pathlist_test', ignore_errors=True)
    try:
        os.remove('iprofile.yml')
    except OSError:
        pass
