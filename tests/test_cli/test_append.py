# -*- coding: utf-8 -*-

from iprofile.cli import Append
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import os
import shutil

mock_options = {
    'name': 'test',
    'path': 'test_append'
}

mock_options_1 = {
    'name': '.',
    'path': 'test_append'
}

mock_options_2 = {
    'name': 'test',
    'path': 'test_append_doesnt_exist'
}

shutil.rmtree('test_append', ignore_errors=True)


def test_append():
    set_up()
    os.mkdir('test_append')
    settings['append'] = {}
    Append.run(mock_options)
    shutil.rmtree('test_append', ignore_errors=True)
    tear_down()


def test_append_project_exists():
    set_up()
    os.mkdir('test_append')
    settings['append'] = {
        'test': 'test_append'
    }
    Append.run(mock_options)
    shutil.rmtree('test_append', ignore_errors=True)
    tear_down()


def test_append_invalid_name():
    set_up()
    Append.run(mock_options_1)
    tear_down()


def test_append_invalid_path():
    set_up()
    Append.run(mock_options_2)
    tear_down()
