# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Delete

try:
    import __builtin__ as builtins
except ImportError:
    import builtins


mock_options_1 = {
    'name': 'test',
}

mock_options_create = {
    'name': 'test2',
}

mock_options_2 = {
    'no_input': True,
    'name': None
}

mock_options_3 = {
    'name': None
}


def test_delete():
    Create.run(mock_options_1)
    Delete.run(mock_options_1)


def test_delete_all_no_input():
    Create.run(mock_options_1)
    Create.run(mock_options_create)
    Delete.run(mock_options_2)


def test_delete_all_confirm_yes(monkeypatch):

    def mock_raw_input(*args, **kwargs):
        return 'y'
    monkeypatch.setattr(builtins, 'raw_input', mock_raw_input)

    Create.run(mock_options_1)
    Create.run(mock_options_create)
    Delete.run(mock_options_3)


def test_delete_all_confirm_no(monkeypatch):

    def mock_raw_input(*args, **kwargs):
        return 'n'
    monkeypatch.setattr(builtins, 'raw_input', mock_raw_input)
    Delete.run(mock_options_3)


def test_delete_none():
    Delete.run(mock_options_2)
