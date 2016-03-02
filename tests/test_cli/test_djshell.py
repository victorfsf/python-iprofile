# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Django
from tests.utils import set_up
from tests.utils import tear_down
import django
import IPython

mock_options_create = {
    'profile': 'test',
    'active': True
}

mock_options = {
    'profile': 'test',
}

mock_options_1 = {
    'profile': 'test',
    'settings': 'test.settings'
}


def mock(monkeypatch):

    def mock_return_none(*args, **kwargs):
        return

    monkeypatch.setattr(IPython, 'start_ipython', mock_return_none)
    monkeypatch.setattr(django, 'setup', mock_return_none)


def mock_raises(monkeypatch):

    def mock_return_none(*args, **kwargs):
        return

    def mock_setup_error(*args, **kwargs):
        raise Exception

    monkeypatch.setattr(IPython, 'start_ipython', mock_return_none)
    monkeypatch.setattr(django, 'setup', mock_setup_error)


def mock_django(monkeypatch):
    try:
        import __builtin__ as builtin
    except ImportError:
        try:
            import builtin
        except ImportError:
            import builtins as builtin

    def mock_return_none(*args, **kwargs):
        return

    orig_import = __import__

    def mock_django_import(name, *args):
        if name == 'django':
            raise ImportError
        return orig_import(name, *args)

    monkeypatch.setattr(IPython, 'start_ipython', mock_return_none)
    monkeypatch.setattr(builtin, '__import__', mock_django_import)


def test_import_django(monkeypatch):
    mock_django(monkeypatch)
    set_up()
    Django.run(mock_options)
    tear_down()


def test_django(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options)
    tear_down()


def test_django_settings(monkeypatch):
    mock(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options_1)
    tear_down()


def test_django_invalid_settings(monkeypatch):
    mock_raises(monkeypatch)
    set_up()
    Create.run(mock_options_create)
    Django.run(mock_options_1)
    tear_down()
