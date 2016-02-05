# -*- coding: utf-8 -*-

from iprofile.core.config import registry


def iregister(command):
    def add_to_registry(command):
        registry.add(command)
        return command
    return add_to_registry(command)
