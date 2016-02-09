# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.cli import Delete
from iprofile.cli import List
import shutil

mock_options = {
    'name': 'test'
}

mock_options_1 = {
    'no_input': True
}

mock_options_2 = {
    'name_only': True
}


def test_run():
    Create.run(mock_options)
    Create.run(mock_options)
    List.run({})
    List.run(mock_options_2)
    Delete.run(mock_options_1)
    List.run({})


def test_no_iprofiles_folder():
    shutil.move('iprofiles', 'iprofiles2')
    List.run({})
    shutil.move('iprofiles2', 'iprofiles')
