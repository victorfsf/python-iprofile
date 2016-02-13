# -*- coding: utf-8 -*-

from iprofile.cli import Init
from iprofile.core.utils import makedirs
import os
import shutil


def test_run():
    Init.run({'path': None})
    makedirs('test_init')
    Init.run({'path': 'test_init'})
    shutil.rmtree('test_init', ignore_errors=True)
    Init.run({'path': 'test_init'})


def test_no_profile_yml():
    try:
        os.remove(os.path.join(os.getcwd(), 'iprofile.yml'))
    except OSError:
        pass
    shutil.rmtree('iprofiles', ignore_errors=True)
    Init.run({'path': None})
