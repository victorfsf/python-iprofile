# -*- coding: utf-8 -*-

from iprofile.cli import Pop
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import os
import shutil

mock_options = {
    'name': 'test',
}

mock_options_1 = {
    'name': '.',
}

mock_options_2 = {
    'name': 'test_doesnt_exist'
}

shutil.rmtree('test_append', ignore_errors=True)


def test_pop():
    set_up()
    os.mkdir('test_append')
    settings['append'] = {
        'test': 'test_append'
    }
    Pop.run(mock_options)
    shutil.rmtree('test_append', ignore_errors=True)
    tear_down()


def test_pop_project_exists():
    set_up()
    Pop.run(mock_options_2)
    tear_down()


def test_pop_invalid_name():
    set_up()
    Pop.run(mock_options_1)
    tear_down()
