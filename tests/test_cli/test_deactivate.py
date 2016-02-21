# -*- coding: utf-8 -*-

from iprofile.cli import Deactivate
from iprofile.cli import Create
from tests.utils import settings
from tests.utils import set_up
from tests.utils import tear_down

mock_options = {
    'profile': 'test',
    'active': True
}


def test_deactivate():
    set_up()
    Create.run(mock_options)
    Deactivate.run({})
    assert settings.get('active') is None
    tear_down()
