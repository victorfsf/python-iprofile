# -*- coding: utf-8 -*-

from iprofile.cli import Init
from iprofile.cli import Create
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import os

mock_options = {
    'path': 'test',
}

mock_options_1 = {
    'path': None,
}

mock_options_2 = {
    'active': 'test',
}

mock_options_3 = {
    'profile': 'test',
}


def test_init():
    Init.run(mock_options)
    assert os.path.isdir(settings.get('path'))
    tear_down()


def test_init_settings_exist():
    set_up()
    Init.run(mock_options)
    tear_down()


def test_init_default_path():
    Init.run(mock_options_1)
    tear_down()


def test_init_active():
    Init.run(mock_options_1)
    Create.run(mock_options_3)
    os.remove('iprofile.yml')
    Init.run(mock_options_2)
    tear_down()


def test_init_profiles_exists():
    Init.run(mock_options_1)
    Create.run(mock_options_3)
    os.remove('iprofile.yml')
    Init.run(mock_options_1)
    tear_down()


def test_init_active_invalid_profile():
    Init.run(mock_options_1)
    os.remove('iprofile.yml')
    Init.run(mock_options_2)
    tear_down()
