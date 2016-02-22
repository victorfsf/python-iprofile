# -*- coding: utf-8 -*-


from iprofile.core.utils import get_user_home
from iprofile.core.utils import echo_plain_red


def test_utils():
    assert '~' not in get_user_home('~/test')
    assert echo_plain_red('test') is None
