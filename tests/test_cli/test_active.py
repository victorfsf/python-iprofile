# -*- coding: utf-8 -*-

from iprofile.cli import Active
from iprofile.cli import Activate
from iprofile.cli import Deactivate
from iprofile.cli import Create
from iprofile.cli import Delete

mock_options = {
    'name': 'test'
}

active = Active.callback(_autorun=False)
result = active.run(**mock_options)
Delete.run(mock_options)
Create.run(mock_options)
Activate.run(mock_options)

def test_name_is_none():
    Deactivate.run({})
    Active.run({})


def test_name_is_not_none():
    Create.run(mock_options)
    Activate.run(mock_options)
    Active.run({})
    Deactivate.run(mock_options)
    Delete.run(mock_options)
