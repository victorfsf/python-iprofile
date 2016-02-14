# -*- coding: utf-8 -*-

import yaml
import os


class GlobalConfig(object):

    def __init__(self):
        self.filepath = os.path.join(os.getcwd(), 'iprofile.yml')
        self._config = {}

        if not os.path.isfile(self.filepath):
            self._config = {
                'project_path': 'iprofiles',
                'project_name': os.path.basename(os.getcwd())
            }
            self.save()

    def read(self):
        self._config = yaml.load(open(self.filepath, 'r')) or {}
        return self.get_all()

    def get(self, value, default=None):
        return self._config.get(value, default)

    def get_all(self):
        return self._config.copy()

    def update(self, kwargs):
        self._config.update(kwargs)
        return self

    def pop(self, key, default=None):
        return self._config.pop(key, default)

    def save(self):
        with open(self.filepath, 'w') as f:
            if self._config:
                f.write(yaml.dump(self._config, default_flow_style=False))
        return self.get_all()


class ProfileConfig(GlobalConfig):

    def __init__(self, path, profile):
        self.filepath = os.path.join(path, profile, 'settings.yml')
        self._config = {}

    def read(self):
        if os.path.isfile(self.filepath):
            return super(ProfileConfig, self).read()
