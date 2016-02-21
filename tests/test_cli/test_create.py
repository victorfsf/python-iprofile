# -*- coding: utf-8 -*-

from iprofile.cli import Create
from tests.utils import settings
from tests.utils import set_up
from tests.utils import tear_down
import os

mock_options = {
    'profile': 'test'
}

mock_options_1 = {
    'profile': '.'
}

mock_options_2 = {
    'profile': 'test',
    'active': True
}


def test_create():
    set_up()
    Create.run(mock_options)
    path = os.path.join(settings.get('path'), 'test')
    assert os.path.isdir(path)
    assert os.path.isfile(os.path.join(path, 'ipython_config.py'))
    tear_down()


def test_create_active():
    set_up()
    Create.run(mock_options_2)
    assert settings.get('active') == 'test'
    tear_down()


def test_invalid_name():
    set_up()
    Create.run(mock_options_1)
    assert not os.listdir(settings.get('path'))
    tear_down()


def test_invalid_profile():
    set_up()
    Create.run(mock_options)
    Create.run(mock_options)
    tear_down()
