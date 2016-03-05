# -*- coding: utf-8 -*-

from iprofile.cli import Delete
from iprofile.cli import Create
from tests.utils import settings
from tests.utils import set_up
from tests.utils import tear_down
import os
import click

mock_options = {
    'profile': 'test',
    'no_input': True,
}

mock_options_1 = {
    'profile': 'test2',
    'no_input': True,
}

mock_options_2 = {
    'no_input': True,
}

mock_options_3 = {
    'profile': 'test',
}

mock_options_4 = {
    'profile': 'test',
    'active': True
}


def mock(monkeypatch):

    def mock_confirm(*args, **kwargs):
        return False

    monkeypatch.setattr(click, 'confirm', mock_confirm)


def test_delete():
    set_up()
    Create.run(mock_options)
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options)
    settings.update({
        'path': 'iprofiles'
    }).save()
    Delete.run(mock_options)
    assert not os.path.isdir(os.path.join(settings.get('path'), 'test'))
    tear_down()


def test_delete_active():
    set_up()
    Create.run(mock_options_4)
    assert settings.get('active') == 'test'
    Delete.run(mock_options_2)
    assert settings.get('active') is None
    tear_down()


def test_delete_all():
    set_up()
    Create.run(mock_options)
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options)
    settings.update({
        'path': 'iprofiles'
    }).save()
    Create.run(mock_options_1)
    Delete.run(mock_options_2)
    assert not os.path.isdir(os.path.join(settings.get('path'), 'test'))
    assert not os.path.isdir(os.path.join(settings.get('path'), 'test2'))
    tear_down()


def test_delete_none():
    set_up()
    Delete.run(mock_options_2)
    tear_down()


def test_invalid_profile():
    set_up()
    Delete.run(mock_options)
    tear_down()


def test_delete_confirm_false(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options)
    Delete.run(mock_options_3)
    tear_down()


def test_delete_none_confirm_false(monkeypatch):
    mock(monkeypatch)
    set_up()
    Delete.run({})
    tear_down()
