# -*- coding: utf-8 -*-

from iprofile.core.models import ICommand
from iprofile.settings.models import Settings
import pytest


def test_run_not_implemented_error():
    with pytest.raises(NotImplementedError):
        ICommand()


def test_icommand_check_settings():
    cmd = ICommand(_autorun=False)
    cmd.settings = Settings()
    cmd.settings.clear()
    assert not cmd.check_settings()


def test_icommand_pred():
    assert ICommand(_autorun=False).pred('test') is None
