# -*- coding: utf-8 -*-


class CommandRegistry(object):

    def __init__(self, *args, **kwargs):
        self.__registry = {}

    def add(self, command):
        self.__registry.update({
            command.name: command
        })

    def get_command(self, name, default=None):
        return self.__registry.get(name, default)


registry = CommandRegistry()
