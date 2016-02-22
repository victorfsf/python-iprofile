# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Shell
from tests.utils import set_up
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


def mock(monkeypatch):

    def mock_start_ipython(*args, **kwargs):
        return

    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)


def test_shell(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Shell.run(mock_options)
    tear_down()


def test_shell_active(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Shell.run(mock_options_1)
    tear_down()


def test_shell_no_profile(monkeypatch):
    mock(monkeypatch)
    set_up()
    Shell.run(mock_options_1)
    tear_down()


def test_shell_invalid_profile(monkeypatch):
    mock(monkeypatch)
    set_up()
    Shell.run(mock_options)
    tear_down()
