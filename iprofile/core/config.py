# -*- coding: utf-8 -*-


class Registry(object):
    __registry = {}

    def add(self, command):
        self.__registry.update({
            command.name: command
        })

    def get_all(self):
        return self.__registry.copy()

    def get_command(self, name, default=None):
        return self.__registry.get(name, default)


registry = Registry()
