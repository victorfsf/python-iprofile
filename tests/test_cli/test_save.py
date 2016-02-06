# -*- coding: utf-8 -*-

from iprofile.cli import Save

mock_options = {
    'name': 'i_do_not_exist'
}


def test_no_profile_to_save():
    Save.run(mock_options)
