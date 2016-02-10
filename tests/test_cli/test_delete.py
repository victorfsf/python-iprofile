# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile.cli import Init
import click
import shutil


mock_options_1 = {
    'name': 'test',
}

mock_options_create = {
    'name': 'test2',
}

mock_options_init = {
    'name': 'test3',
}

mock_options_2 = {
    'no_input': True,
}

mock_options_3 = {
    'name': None
}


def test_delete():
    Create.run(mock_options_1)
    Delete.run(mock_options_1)

    Init.run(mock_options_init)
    Delete.run(mock_options_init)


def test_delete_no_iprofiles_folder():
    shutil.move('iprofiles', 'iprofiles2')
    Delete.run(mock_options_1)
    shutil.move('iprofiles2', 'iprofiles')


def test_delete_all_no_input():
    Create.run(mock_options_1)
    Create.run(mock_options_create)
    Delete.run(mock_options_2)


def test_delete_all_confirm_yes(monkeypatch):

    def mock_confirm(*args, **kwargs):
        return True

    monkeypatch.setattr(click, 'confirm', mock_confirm)
    Create.run(mock_options_1)
    Create.run(mock_options_create)
    Delete.run(mock_options_3)


def test_delete_all_confirm_no(monkeypatch):

    def mock_confirm(*args, **kwargs):
        return False

    monkeypatch.setattr(click, 'confirm', mock_confirm)
    Delete.run(mock_options_3)


def test_delete_none():
    Delete.run(mock_options_2)
