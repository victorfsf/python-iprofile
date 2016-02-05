# -*- coding: utf-8 -*-

from iprofile.core.config import registry
import sys


class IProfile(object):

    def __init__(self, argv, *args, **kwargs):
        if len(argv) == 1:
            return
        name = argv.pop(1)
        command = registry.get_command(name)
        if not command:
            return
        command()

IProfile(argv=sys.argv)
