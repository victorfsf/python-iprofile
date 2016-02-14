# -*- coding: utf-8 -*

from slugify import slugify
from iprofile.core.utils import get_ipython_name
from iprofile.core.utils import get_user_home
from iprofile.models import ProfileConfig
import IPython
import os
import subprocess


class Profile(object):

    def __init__(self, name, config, **kwargs):
        self.name = slugify(name.strip()) if name else None

        if not self.name:
            return

        directory = kwargs.pop('directory', None)
        self.directory = (
            os.path.abspath(get_user_home(directory)) if directory else None
        )

        self.ipython_name = get_ipython_name(self.name, config)
        self.config = ProfileConfig(config.get('project_path'), self.name)
        self.config.read()

        profile_path = os.path.abspath(
            os.path.join(config.get('project_path'), self.name))

        self._path = {
            'profile': profile_path,
            'settings': os.path.join(profile_path, 'settings.yml'),
            'startup': os.path.join(profile_path, 'startup'),
            'config': os.path.join(profile_path, 'ipython_config.py'),
        }

        self.ipython_locate()

    def path(self, value, default=None):
        return self._path.get(value, default)

    def exists(self):
        if os.path.isfile(self.path('settings')):
            return True
        return False

    def ipython_exists(self):
        ipython_path = self.path('ipython')
        if ipython_path and os.path.isdir(ipython_path):
            return True
        return False

    def ipython_create(self):
        args = 'ipython profile create {0}'.format(self.ipython_name).split()
        if self.directory:
            if not os.path.isdir(self.directory):
                os.makedirs(self.directory)
            args += ['--profile-dir', '"{0}"'.format(self.directory)]
        process = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        return self.ipython_locate()

    def ipython_locate(self):
        if not self.directory:
            self.directory = self.config.get('ipython_path')

        try:
            result = self.directory or IPython.paths.locate_profile(
                self.ipython_name)

            if result:
                abs_ipython_path = os.path.abspath(result)
                self._path.update({
                    'ipython': abs_ipython_path,
                    'ipython_startup': os.path.join(
                        abs_ipython_path, 'startup'),
                    'ipython_config': os.path.join(
                        abs_ipython_path, 'ipython_config.py')
                })
                return result
        except IOError:
            return
