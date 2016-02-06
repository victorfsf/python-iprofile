# -*- coding: utf-8 -*-

from iprofile import console
from iprofile.core.config import registry
from iprofile.cli import *  # noqa
import pytest
import sys


def test_iprofile_class():
    iprofile = console.IProfile()
    assert iprofile.list_commands({}) == sorted(registry.get_all())
    assert iprofile.get_command({}, 'shell') == registry.get_command('shell')


def test_main():
    console.main.callback()
    with pytest.raises(SystemExit):
        sys.argv = []
        console.main()
