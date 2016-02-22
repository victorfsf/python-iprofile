# -*- coding: utf-8 -*-

from iprofile.cli import Create
from iprofile.profiles.models import IProfileDir
from tests.utils import settings
from tests.utils import set_up
from tests.utils import tear_down
from os.path import join
from os.path import isfile
import shutil

mock_options = {
    'profile': 'test'
}


def test_check_dirs():
    set_up()
    Create.run(mock_options)
    path = join(settings.get('path'), 'test')
    profile_dir = IProfileDir.find_profile_dir(path)
    shutil.rmtree(profile_dir.startup_dir, ignore_errors=True)
    profile_dir.check_dirs()
    assert isfile(join(profile_dir.startup_dir, '00_config.ipy'))
    assert isfile(join(profile_dir.startup_dir, '01_scripts.py'))
    tear_down()
