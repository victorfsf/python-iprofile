# -*- coding: utf-8 -*-

from iprofile.cli import Config
from iprofile.settings.models import SectionDict
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down

mock_options = {
    'name': 'test_name',
    'value': 'test_value'
}

mock_options_1 = {
    'name': 'test_name',
    'value': '["test_value"]'
}

mock_options_2 = {
    'name': 'test_name',
    'value': '{"test_value": 0}'
}


def test_config():
    set_up()
    Config.run(mock_options)
    assert settings.get('test_name') == 'test_value'
    tear_down()


def test_config_list_or_dict():
    set_up()

    Config.run(mock_options_1)
    assert isinstance(settings.get('test_name'), list)
    assert len(settings.get('test_name')) == 1
    assert settings.get('test_name')[0] == 'test_value'

    Config.run(mock_options_2)
    assert isinstance(settings.get('test_name'), SectionDict)
    assert 'test_value' in settings.get('test_name')
    assert settings.get('test_name').get('test_value') == 0

    tear_down()
