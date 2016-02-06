# -*- coding: utf-8 -*-

from iprofile.core.models import ICommand
import pytest


def test_run_not_implemented_error():
    with pytest.raises(NotImplementedError):
        ICommand()
