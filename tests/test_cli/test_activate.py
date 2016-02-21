# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from tests.utils import settings
from tests.utils import set_up
from tests.utils import tear_down

mock_options = {
    'profile': 'test'
}

mock_options_1 = {
    'profile': '.'
}


def test_activate():
    set_up()
    Create.run(mock_options)
    Activate.run(mock_options)
    assert settings.get('active') == 'test'
    tear_down()


def test_invalid_name():
    set_up()
    Activate.run(mock_options_1)
    assert settings.get('active') is None
    tear_down()


def test_invalid_profile():
    set_up()
    Activate.run(mock_options)
    assert settings.get('active') is None
    tear_down()
