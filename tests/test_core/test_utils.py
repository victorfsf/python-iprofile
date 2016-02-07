# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Activate
from iprofile.cli import Deactivate
from iprofile.cli import Delete
from iprofile.core.utils import get_active_profile

mock_options = {
    'name': 'test'
}


def test_get_active_profile():
    Create.run(mock_options)
    Activate.run(mock_options)
    assert get_active_profile() == 'test'
    Deactivate.run({})
    assert get_active_profile() is None
    Delete.run(mock_options)
