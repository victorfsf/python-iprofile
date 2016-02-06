# -*- coding: utf-8 -*-

from iprofile.cli import texts
from iprofile.core.config import registry
from iprofile.core.utils import echo_red
import click
import sys


class IProfile(object):
    """IProfile CLI

A CLI for handling IPython 4+ profiles startup scripts.

usage: iprofile <command> [<options>] <args>

\b
Commands:
    init\tCreate a new profile
    create\tCreate a new profile and save it on IPython's profiles path
    save\tSave changes to IPython's path
    clear\tRemove the profile from IPython's path, but still keeps it locally
    delete\tCompletely delete the profile
    """

    def __init__(self, argv, *args, **kwargs):
        if len(argv) == 1:
            click.echo(self.__doc__)
            return
        name = argv.pop(1)
        command = registry.get_command(name)
        if not command:
            echo_red(texts.ERROR_COMMAND_NOT_FOUND.format(name))
            click.echo('\n' + self.__doc__)
            return
        command()


def main():
    IProfile(argv=sys.argv)


if __name__ == '__main__':
    main()
