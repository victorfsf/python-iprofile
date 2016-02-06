# -*- coding: utf-8 -*-

from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Deactivate
from iprofile.cli import Delete

mock_options = {
    'name': 'test'
}

Delete.run(mock_options)
Create.run(mock_options)


def test_run():
    Activate.run(mock_options)
    Deactivate.run({})
