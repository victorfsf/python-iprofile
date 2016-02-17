# -*- coding: utf-8 -*-

from collections import OrderedDict
import yaml


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
            return yaml.load(open(self.filepath, 'r'))
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

    def pop(self, value, default=None):
        super(YAMLOrderedDict, self).pop(value, default)
        return self

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


class Settings(YAMLOrderedDict):
    default = {}
