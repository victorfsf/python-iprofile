# -*- coding: utf-8 -*-

from iprofile.cli import Shell
from iprofile.cli import Create
from iprofile.cli import Activate
from iprofile.cli import Deactivate

mock_options = {
    'name': 'test'
}

Create.run(mock_options)
shell = Shell.callback(_autorun=False)


def test_get_active_profile():
    Activate.run(mock_options)
    assert shell.get_active_profile() == 'test'
    Deactivate.run({})
    assert shell.get_active_profile() is None
