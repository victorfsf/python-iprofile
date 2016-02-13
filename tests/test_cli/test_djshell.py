# -*- coding: utf-8 -*-

from iprofile.cli import Django
from iprofile.cli import Config
import django
import IPython

mock_options = {
    'name': None
}

mock_options_1 = {
    'name': 'django_settings_module',
    'value': 'test_module'
}


def test_run(monkeypatch):

    def mock_setup(*args, **kwargs):
        return

    def mock_start_ipython(*args, **kwargs):
        return

    monkeypatch.setattr(django, 'setup', mock_setup)
    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)
    Django.run(mock_options)
    Config.run(mock_options_1)
    Django.run(mock_options)


def test_run_import_error(monkeypatch):
    def mock_setup(*args, **kwargs):
        raise ImportError

    def mock_start_ipython(*args, **kwargs):
        return

    monkeypatch.setattr(django, 'setup', mock_setup)
    monkeypatch.setattr(IPython, 'start_ipython', mock_start_ipython)
    Config.run(mock_options_1)
    Django.run(mock_options)
