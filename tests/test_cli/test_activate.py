# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile import texts
from iprofile.models import GlobalConfig

mock_options = {
    'name': 'test'
}

mock_options_1 = {
    'name': 'test2'
}

activate = Activate.callback(_autorun=False)
result = activate.run(**mock_options)
Delete.run(mock_options)
Create.run(mock_options)


def test_run():
    activate.green(texts.LOG_PROFILE_ACTIVATED.format('test'))
    activate.activate_profile('test')
    activate.run(**mock_options_1)


def test_activate_profile():
    config = GlobalConfig()
    config.read()
    activate.activate_profile('test')
    assert config.get('active_profile') == 'test'
