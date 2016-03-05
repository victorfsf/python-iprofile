# -*- coding: utf-8 -*-

from collections import OrderedDict
from iprofile.utils.mixins import OSMixin
import os
import yaml


class YAMLOrderedDict(OrderedDict, OSMixin):
    base_section = 'settings'
    default = {}

    def __init__(self, path, *args, **kwargs):
        self.default = kwargs.pop('default', self.default)
        super(YAMLOrderedDict, self).__init__(*args, **kwargs)
        self.path = path
        self.dirname = self.dirname(path)
        self.default_flow_style = kwargs.pop('default_flow_style', False)
        self.indent = kwargs.pop('indent', 4)
        self.__loaded = False

    def read(self, ignore_errors=False):
        update = super(YAMLOrderedDict, self).update
        try:
            data = update(self.open())
        except IOError:
            if ignore_errors:
                data = update(self.create())
            else:
                data = {}
        self.__loaded = True
        return data

    def create(self):
        self.make_settings_path()
        with open(self.path, 'w') as f:
            f.write(self.dump({self.base_section: self.default}))
        return self.default

    def update(self, data):
        super(YAMLOrderedDict, self).update(data)
        return self

    def pop(self, value, default=None):
        return super(YAMLOrderedDict, self).pop(value, default)

    def save(self):
        self.make_settings_path()
        with open(self.path, 'w') as f:
            f.write(self.dump({self.base_section: dict(self)}))
        return self

    def dump(self, data):
        return yaml.dump(
            data,
            default_flow_style=self.default_flow_style,
            indent=self.indent
        )

    def open(self):
        yaml_dict = yaml.load(open(self.path, 'r'))
        if not (yaml_dict and yaml_dict.get(self.base_section)):
            return self.create()
        return yaml_dict.get(self.base_section)

    def make_settings_path(self):
        return self.makedirs(os.path.dirname(self.path))

    def exists(self):
        return True if self.isfile(self.path) and self.__loaded else False

    def get(self, key, default=None):
        get_def = 'get_{}'.format(key)
        value = super(YAMLOrderedDict, self).get(key, default)
        if hasattr(self, get_def):
            return getattr(self, get_def)(value)
        return value
