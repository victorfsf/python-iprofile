# -*- coding: utf-8 -*-

from iprofile.core.config import registry
import click
import sys


class IProfile(object):

    def __init__(self, argv, *args, **kwargs):
        if len(argv) == 1:
            click.echo("# TODO: ADD COMMAND LINE HELP")
            return
        name = argv.pop(1)
        command = registry.get_command(name)
        if not command:
            return
        command()


def main():
    IProfile(argv=sys.argv)


if __name__ == '__main__':
    main()
