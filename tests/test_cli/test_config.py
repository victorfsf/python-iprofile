# -*- coding: utf-8 -*-

from iprofile.cli import Config

mock_options = {
    'name': 'test',
    'value': 'test',
    'profile': 'test'
}


def test_run():
    Config.run(mock_options)
