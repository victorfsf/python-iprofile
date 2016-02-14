# -*- coding: utf-8 -*-

from iprofile.cli import Add
from iprofile.cli import Magic
import shutil

mock_options_add = {
    'name': 'test',
}

mock_options = {
    'profile': 'test',
    'script': 'autoreload',
    'filename': None
}

mock_options_1 = {
    'profile': 'test',
    'script': 'autoreload',
    'filename': '00_autoreload'
}

mock_options_2 = {
    'profile': 'test',
    'script': 'autoreload2',
    'filename': None
}

mock_options_3 = {
    'profile': None,
    'script': 'autoreload',
    'filename': None
}


def test_run():
    Magic.run(mock_options)
    Magic.run(mock_options_1)
    Magic.run(mock_options_2)
    Magic.run(mock_options_3)

    Add.run(mock_options_add)
    Magic.run(mock_options)
    Magic.run(mock_options_1)

    shutil.rmtree('iprofiles/test/startup', ignore_errors=True)
    Magic.run(mock_options)
