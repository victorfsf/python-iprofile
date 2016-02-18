# -*- coding: utf-8 -*-

from collections import OrderedDict
import yaml


class SectionDict(object):

    def __init__(self, basedict, *args, **kwargs):
        self.__basedict = basedict
        self.__map = kwargs.pop('map', None)

    def __getattr__(self, name):
        return getattr(self.__map, name)

    def __getitem__(self, key):
        return self.__map[key]

    def __setitem__(self, key, value):
        self.__map[key] = value
        return self.__map

    def get(self, value, default=None):
        result = self.__map.get(value, default)
        if result and isinstance(result, dict):
            return SectionDict(self.__map, map=result)
        return result

    def update(self, data):
        self.__map.update(data)
        return self.__map

    def pop(self, value, default=None):
        return self.__map.pop(value, default)

    def __repr__(self):
        return str(self.__map)


class YAMLOrderedDict(OrderedDict):
    default = {}

    def __init__(self, filepath, *args, **kwargs):
        super(YAMLOrderedDict, self).__init__()
        self.filepath = filepath
        self.default = kwargs.pop('default', self.default)
        data = self.read()
        if data:
            super(YAMLOrderedDict, self).update(data)
        delattr(self, 'default')

    def read(self):
        try:
            return self.load()
        except IOError:
            self.create()
        return self.default

    def create(self):
        with open(self.filepath, 'w') as f:
            f.write(self.dump(self.default))
        return self

    def update(self, data):
        super(YAMLOrderedDict, self).update(data)
        return self

    def get(self, value, default=None):
        result = super(YAMLOrderedDict, self).get(value, default)
        if result and isinstance(result, dict):
            return SectionDict(self, map=result)
        return result

    def pop(self, value, default=None):
        return super(YAMLOrderedDict, self).pop(value, default)

    def save(self):
        with open(self.filepath, 'w') as f:
            f.write(self.dump(dict(self)))
        return self

    def dump(self, data):
        return yaml.dump(
            data,
            default_flow_style=False,
            indent=4
        )

    def load(self):
        return yaml.load(open(self.filepath, 'r'))


class Settings(YAMLOrderedDict):
    default = {
        'profiles': {
            'path': 'iprofiles',
            'active': None
        }
    }
