# -*- coding: utf-8 -*-

from collections import OrderedDict
from iprofile.utils.mixins import OSMixin
import os
import yaml


class SectionDict(dict):

    def __init__(self, yamlmap, basemap, *args, **kwargs):
        self.__basemap = basemap
        self.__yamlmap = yamlmap
        super(SectionDict, self).__init__(kwargs.pop('map'), *args, **kwargs)

    def get(self, value, default=None):
        result = super(SectionDict, self).get(value, default)
        if result and isinstance(result, dict):
            return SectionDict(self.__yamlmap, self, map=result)
        return result

    def update(self, data):
        super(SectionDict, self).update(data)
        return self.__yamlmap

    def pop(self, value, default=None):
        return super(SectionDict, self).pop(value, default)

    def save(self):
        return self.__yamlmap.save()


class YAMLOrderedDict(OrderedDict, OSMixin):
    default = {}

    def __init__(self, path, *args, **kwargs):
        self.default = kwargs.pop('default', self.default)
        super(YAMLOrderedDict, self).__init__(*args, **kwargs)
        self.path = path
        self.default_flow_style = kwargs.pop('default_flow_style', False)
        self.indent = kwargs.pop('indent', 4)
        self.__loaded = False

    def read(self):
        update = super(YAMLOrderedDict, self).update
        try:
            data = update(self.load())
        except IOError:
            data = update(self.create())
        self.__loaded = True
        return data

    def create(self):
        self.make_settings_path()
        with open(self.path, 'w') as f:
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
        with open(self.path, 'w') as f:
            f.write(self.dump(dict(self)))
        return self

    def dump(self, data):
        return yaml.dump(
            data,
            default_flow_style=self.default_flow_style,
            indent=self.indent
        )

    def load(self):
        return yaml.load(open(self.path, 'r'))

    def make_settings_path(self):
        return self.makedirs(os.path.dirname(self.path))

    def exists(self):
        return True if self.isfile(self.path) and self.__loaded else False


class SettingsBase(YAMLOrderedDict):
    base_section = None

    def load(self):
        yaml_dict = yaml.load(open(self.path, 'r'))
        if not yaml_dict.get(self.base_section):
            return self.create()
        return yaml_dict
