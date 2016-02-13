# -*- coding: utf-8 -*-

from iprofile.core.utils import get_user_home
import os


mock_options = {
    'name': 'test',
}

mock_options_1 = {
    'name': 'test',
    'profile_dir': '~/.ipython/profile_python-iprofile_test'
}


def test_get_user_home():
    assert get_user_home('~/test') == os.path.join(
        os.path.expanduser('~'), 'test')
