# -*- coding: utf-8 -*-

from iprofile.cli import Active
from iprofile.cli import Activate
from iprofile.cli import Create
from iprofile.cli import Delete
import os

mock_options = {
    'name': 'test'
}

active = Active.callback(_autorun=False)
result = active.run(**mock_options)
Delete.run(mock_options)
Create.run(mock_options)
Activate.run(mock_options)


def test_get_active_profile():
    assert active.get_active_profile() == 'test'
    os.remove('{}/.active'.format(active.project_path))
    assert active.get_active_profile() is None


def test_end():
    Delete.run(mock_options)