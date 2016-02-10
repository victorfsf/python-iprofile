# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile.cli import Init
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


def test_run(monkeypatch):

    def mock_start_ipython(*args, **kwargs):
        return None

    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)
    Shell.run({})
    Create.run(mock_options)
    Shell.run(mock_options)
    Delete.run(mock_options)
    Shell.run(mock_options)

    Init.run(mock_options_1)
    Shell.run(mock_options_1)

    Delete.run(mock_options_2)
    Shell.run(mock_options_1)
