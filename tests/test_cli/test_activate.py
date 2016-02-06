# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile import texts

mock_options = {
    'name': 'test'
}

activate = Activate.callback(_autorun=False)
result = activate.run(**mock_options)
Delete.run(mock_options)
Create.run(mock_options)


def test_run():
    assert activate.green(texts.LOG_PROFILE_ACTIVATED.format('test')) is None
    assert activate.activate_profile('test') is None


def test_activate_profile():
    active_path = '{}/.active'.format(activate.project_path)
    assert activate.activate_profile('test') is None
    with open(active_path, 'r') as active:
        assert active.read() == 'test'


def test_end():
    Delete.run(mock_options)
