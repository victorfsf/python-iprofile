# -*- coding: utf-8 -*-

from ishell.config import registry
from ishell.profile import *  # noqa
import os
import sys


class IShell(object):

    def __init__(self, argv, *args, **kwargs):
        argv.pop(0)
        if not argv:
            raise AttributeError("No command given.")
        command_name = argv.pop(0)
        command = registry.get_command(command_name)
        if not command:
            raise AttributeError(
                "The command '{}' does not exist.".format(command_name))
        command(argv=argv, path=os.getcwd())


def main():
    IShell(sys.argv)
