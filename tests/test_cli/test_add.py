# -*- coding: utf-8 -*-

from iprofile.cli import Add
from iprofile.models import GlobalConfig
import os
import shutil

mock_options = {
    'name': 'test',
    'no_symlink': True
}

mock_options_1 = {
    'name': 'test2',
    'autoreload': True
}

add = Add.callback(_autorun=False)
add.run(**mock_options)


def test_run():
    config = GlobalConfig()
    config.read()
    shutil.rmtree(config.get('project_path'))
    Add.run(mock_options)
    assert os.path.isdir(config.get('project_path'))
    Add.run(mock_options_1)
