# -*- coding: utf-8 -*-

from iprofile.cli import Init
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
