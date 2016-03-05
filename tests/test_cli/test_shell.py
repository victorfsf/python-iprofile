# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Shell
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import IPython

mock_options_create = {
    'profile': 'test',
    'active': True
}

mock_options = {
    'profile': 'test',
}

mock_options_1 = {
    'profile': None,
}

mock_options_2 = {
    'profile': 'test',
    'project': 'test'
}


def mock(monkeypatch):

    def mock_start_ipython(*args, **kwargs):
        return

    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)


def test_shell(monkeypatch):
    mock(monkeypatch)
    set_up()
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options)
    settings.update({
        'path': 'iprofiles'
    }).save()
    Shell.run(mock_options)
    Shell.run(mock_options_2)
    tear_down()


def test_shell_active(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Shell.run(mock_options_1)
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options_create)
    settings.update({
        'path': 'iprofiles'
    }).save()
    Activate.run(mock_options_2)
    Shell.run(mock_options_1)
    tear_down()


def test_shell_no_profile(monkeypatch):
    mock(monkeypatch)
    set_up()
    settings.update({
        'append': {
            'test': None
        }
    }).save()
    Shell.run(mock_options_1)
    tear_down()


def test_shell_profile_none(monkeypatch):
    mock(monkeypatch)
    set_up()
    settings.update({
        'append': {
            'test': None
        }
    }).save()
    Shell.run(mock_options_2)
    tear_down()


def test_shell_invalid_profile(monkeypatch):
    mock(monkeypatch)
    set_up()
    Shell.run(mock_options)
    tear_down()


def test_shell_other_project_profile(monkeypatch):
    mock(monkeypatch)
    set_up()
    Shell.run(mock_options)
    tear_down()
