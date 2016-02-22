# -*- coding: utf-8 -*-

from collections import OrderedDict
from iprofile.utils.mixins import OSMixin
import os
import yaml


class SectionDict(object):

    def __init__(self, yamlmap, basemap, *args, **kwargs):
        self.__basemap = basemap
        self.__yamlmap = yamlmap
        self.__map = kwargs.pop('map')
        super(SectionDict, self).__init__(*args, **kwargs)

    def __iter__(self):
        return iter(self.__map)

    def __repr__(self):
        return str(self.__map)

    def get(self, value, default=None):
        if '.' not in value:
            result = self.__map.get(value, default)
            if result and isinstance(result, dict):
                return SectionDict(self.__yamlmap, self.__map, map=result)
            return result
        paths = value.split('.')
        data = self.get(paths[0], default)
        if isinstance(data, SectionDict):
            return SectionDict(
                self.__yamlmap, self.__map, map=data).get(
                    '.'.join(paths[1:]), default)
        if len(paths) > 1:
            return

    def update(self, data):
        self.__map.update(data)
        return self.__yamlmap

    def pop(self, value, default=None):
        return self.__map.pop(value, default)

    def save(self):
        return self.__yamlmap.save()


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
