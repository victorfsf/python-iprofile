# -*- coding: utf-8 -*-

from iprofile.core.models import ICommand
from iprofile.cli import Create
from iprofile.settings.models import Settings
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import pytest


mock_options = {
    'profile': 'test'
}


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


def test_icommand_list_profiles():
    set_up()
    settings.update({
        'path': 'append_test'
    }).save()
    Create.run(mock_options)
    settings.update({
        'path': 'iprofiles'
    }).save()
    cmd = ICommand(_autorun=False)
    cmd.settings = settings
    cmd.list_profiles('iprofiles')
    tear_down()
