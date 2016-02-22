# -*- coding: utf-8 -*-

from iprofile.profiles.utils import list_profiles
from iprofile.profiles.utils import get_ipython_dir
import IPython


def test_profiles_utils():
    assert not list_profiles('test_path')
    assert get_ipython_dir() == IPython.paths.get_ipython_dir()
