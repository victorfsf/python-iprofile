# -*- coding: utf-8 -*-

from iprofile.cli import Add
from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile.cli import Save
import os


mock_options = {
    'name': 'i_do_not_exist'
}

mock_options_1 = {
    'name': 'test1',
}

mock_options_2 = {
    'name': 'test2',
    'profile_dir': '~/test_profile/'
}

mock_options_3 = {
    'name': None
}

mock_options_4 = {
    'name': None,
    'no_input': True
}

mock_options_5 = {
    'name': 'test5',
    'no_symlink': True
}


def test_no_profile_to_save():
    Save.run(mock_options)


def test_remove():
    filename = 'test.txt'
    symlink = 'testlink.txt'

    try:
        os.unlink(symlink)
        os.remove(filename)
    except OSError:
        pass

    open(filename, 'w').close()
    os.symlink(filename, symlink)
    Save.callback(_autorun=False).remove(symlink)
    Save.callback(_autorun=False).remove(filename)


def test_save_all():
    Add.run(mock_options_1)
    Add.run(mock_options_2)
    Save.run(mock_options_3)
    Create.run(mock_options_5)
    Delete.run(mock_options_4)
