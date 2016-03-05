# -*- coding: utf-8 -*-

from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import os


def test_yamlordereddict_pop():
    set_up()
    path = settings.get('path')
    assert os.path.abspath(os.path.expanduser(settings.pop('path'))) == path
    tear_down()


def test_yamlordereddict_open():
    set_up()
    settings.base_section = None
    settings.open()
    tear_down()
