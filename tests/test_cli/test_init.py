# -*- coding: utf-8 -*-

from iprofile.cli import Init
from iprofile.cli import Save
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import PROJECT_PATH
import os
import shutil

mock_options = {
    'name': 'test',
    'no_symlink': True
}

init = Init.callback(_autorun=False)
init.run(**mock_options)


def test_run():
    shutil.rmtree(PROJECT_PATH)
    Init.run(mock_options)
    assert os.path.isdir(PROJECT_PATH)


def test_check_ipython():
    Save.run(mock_options)
    shutil.rmtree(get_profile_path('test'))
    assert init.check_ipython('test', get_profile_path('test')) is True
