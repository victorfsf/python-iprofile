# -*- coding: utf-8 -*-

from iprofile.core.utils import GLOBAL_SETTINGS_FILE
from iprofile.models import ICommand
from iprofile.models import GlobalConfig
import pytest
import os


def test_run_not_implemented_error():
    with pytest.raises(NotImplementedError):
        ICommand()


def test_iprofiles_yml_does_not_exist():
    try:
        os.remove(GLOBAL_SETTINGS_FILE)
    except OSError:
        pass
    GlobalConfig()
