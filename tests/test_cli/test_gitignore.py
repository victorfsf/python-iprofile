# -*- coding: utf-8 -*-

from iprofile.cli import GitIgnore
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down
import os


def test_gitignore():
    set_up()
    gitignore = GitIgnore.callback(_autorun=False)
    gitignore.run()

    filepath = os.path.join(settings.get('path'), '.gitignore')
    assert os.path.isfile(filepath)
    with open(filepath, 'r') as f:
        assert f.read() == '\n'.join(gitignore.content)

    gitignore.run()
    tear_down()
