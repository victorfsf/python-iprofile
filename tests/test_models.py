# -*- coding: utf-8 -*-

from iprofile.models import ICommand
from iprofile.models import GlobalConfig
from iprofile.models import Profile
import pytest
import os


def test_run_not_implemented_error():
    with pytest.raises(NotImplementedError):
        ICommand()


def test_iprofiles_yml_does_not_exist():
    try:
        os.remove('iprofiles.yml')
    except OSError:
        pass
    GlobalConfig()
