# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Active
from iprofile.cli import Create
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down

mock_options = {
    'profile': 'test'
}

mock_options_1 = {
    'profile': '.'
}


def test_active():
    set_up()
    Create.run(mock_options)
    Activate.run(mock_options)
    Active.run({})
    tear_down()


def test_no_active_profile():
    set_up()
    Active.run({})
    tear_down()


def test_invalid_profile():
    set_up()
    settings.update({
        'active': 'test'
    }).save()
    Active.run({})
    tear_down()
