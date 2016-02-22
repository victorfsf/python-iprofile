# -*- coding: utf-8 -*-

from iprofile.cli import List
from iprofile.cli import Create
from tests.utils import set_up
from tests.utils import tear_down

mock_options = {
    'profile': 'test',
}

mock_options_1 = {
    'profile': 'test1',
}

mock_options_2 = {
    'profile': 'test2',
}

mock_options_3 = {
    'profile': 'test3',
    'active': True
}


def test_list():
    set_up()
    Create.run(mock_options)
    Create.run(mock_options_1)
    Create.run(mock_options_2)
    List.run({})
    tear_down()


def test_list_names_only():
    set_up()
    Create.run(mock_options)
    Create.run(mock_options_1)
    Create.run(mock_options_2)
    List.run({})
    tear_down()


def test_list_no_profiles():
    set_up()
    List.run({})
    tear_down()


def test_list_active_profile():
    set_up()
    Create.run(mock_options_3)
    List.run({})
    tear_down()
