# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Deactivate
from iprofile.cli import Delete

mock_options = {
    'name': 'test'
}


def test_run():
    Activate.run(mock_options)
    Delete.run(mock_options)
    Create.run(mock_options)
    Activate.run(mock_options)
    Deactivate.run({})
    Deactivate.run({})
