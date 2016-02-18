# -*- coding: utf-8 -*-

from collections import OrderedDict
import os
import yaml


class SectionDict(object):

    def __init__(self, yamlmap, basemap, *args, **kwargs):
        self.__basemap = basemap
        self.__yamlmap = yamlmap
        self.__map = kwargs.pop('map', None)

    def __getattr__(self, name):
        return getattr(self.__map, name)

    def __getitem__(self, key):
        return self.__map[key]

    def __setitem__(self, key, value):
        self.__map[key] = value
        return self.__yamlmap

    def __repr__(self):
        return str(self.__map)

    def get(self, value, default=None):
        result = self.__map.get(value, default)
        if result and isinstance(result, dict):
            return SectionDict(self.__yamlmap, self.__map, map=result)
        return result

    def update(self, data):
        self.__map.update(data)
        return self.__yamlmap

    def pop(self, value, default=None):
        return self.__map.pop(value, default)

    def save(self):
        return self.__yamlmap.save()


class YAMLOrderedDict(OrderedDict):
    default = {}

    def __init__(self, filepath, *args, **kwargs):
        super(YAMLOrderedDict, self).__init__(*args, **kwargs)
        self.filepath = filepath
        self.default = kwargs.pop('default', self.default)
        self.default_flow_style = kwargs.pop('default_flow_style', False)
        self.indent = kwargs.pop('indent', 4)
        data = self.read()
        if data:
            super(YAMLOrderedDict, self).update(data)

    def read(self):
        try:
            return self.load()
        except IOError:
            return self.create()

    def create(self):
        self.make_settings_path()
        with open(self.filepath, 'w') as f:
            f.write(self.dump(self.default))
        return self.default

    def update(self, data):
        super(YAMLOrderedDict, self).update(data)
        return self

    def get(self, value, default=None):
        result = super(YAMLOrderedDict, self).get(value, default)
        if result and isinstance(result, dict):
            return SectionDict(self, self, map=result)
        return result

    def pop(self, value, default=None):
        return super(YAMLOrderedDict, self).pop(value, default)

    def save(self):
        self.make_settings_path()
        with open(self.filepath, 'w') as f:
            f.write(self.dump(dict(self)))
        return self

    def dump(self, data):
        return yaml.dump(
            data,
            default_flow_style=self.default_flow_style,
            indent=self.indent
        )

    def load(self):
        return yaml.load(open(self.filepath, 'r'))

    def join(self, *args):
        return os.path.join(*args)

    def makedirs(self, path):
        try:
            os.makedirs(path)
        except OSError:
            pass

    def make_settings_path(self):
        return self.makedirs(os.path.dirname(self.filepath))


class SettingsBase(YAMLOrderedDict):
    base_section = None

    def load(self):
        yaml_dict = yaml.load(open(self.filepath, 'r'))
        if not yaml_dict.get(self.base_section):
            return self.create()
        return yaml_dict
