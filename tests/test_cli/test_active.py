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

mock_options_2 = {
    'profile': 'test',
    'project': 'test'
}


def test_active():
    set_up()
    Create.run(mock_options)
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options)
    settings.update({
        'path': 'iprofiles'
    }).save()
    Activate.run(mock_options)
    Active.run({})
    Activate.run(mock_options_2)
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
