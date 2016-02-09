# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Activate
from iprofile.cli import Deactivate
from iprofile.cli import Delete
from iprofile.core.utils import get_active_profile
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import read_config
from iprofile.core.utils import create_ipython_profile
from iprofile.core.utils import get_user_home


mock_options = {
    'name': 'test',
}

mock_options_1 = {
    'name': 'test',
    'profile_dir': '~/.ipython/profile_python-iprofile_test'
}


def test_get_active_profile():
    Create.run(mock_options)
    Activate.run(mock_options)
    assert get_active_profile() == 'test'
    Deactivate.run({})
    assert get_active_profile() is None
    Delete.run(mock_options)


def test_get_profile_path():
    Create.run(mock_options)
    directory = get_user_home('~/.ipython/profile_python-iprofile_test')
    get_ipython_path('test', directory)
    Delete.run(mock_options)


def test_read_config():
    Create.run(mock_options)
    path = get_profile_path('test')
    config_file = path + '/.config'
    with open(config_file, 'w') as f:
        f.write('PROFILE_DIR=~/.ipython/profile_python-iprofile_test')
    read_config(config_file)
    Delete.run(mock_options)


def test_create_ipython_profile():
    Create.run(mock_options)
    directory = get_user_home('~/.ipython/profile_python-iprofile_test2')
    create_ipython_profile('test', directory)
    Delete.run(mock_options)
