# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Activate
from iprofile.cli import Delete
from iprofile.cli import Add
from iprofile.cli import Shell
import IPython

mock_options = {
    'name': 'test'
}

mock_options_1 = {
    'name': 'testshell'
}

mock_options_2 = {
    'no_input': True
}

mock_options_3 = {
    'no_profile': True
}

mock_options_4 = {
    'name': None
}


def test_run(monkeypatch):

    def mock_start_ipython(*args, **kwargs):
        return None

    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)
    Shell.run({})
    Create.run(mock_options)
    Shell.run(mock_options)
    Delete.run(mock_options)
    Shell.run(mock_options)

    Add.run(mock_options_1)
    Shell.run(mock_options_1)

    Activate.run(mock_options_1)
    Shell.run(mock_options_4)

    Delete.run(mock_options_2)
    Shell.run(mock_options_1)
    Shell.run(mock_options_3)
