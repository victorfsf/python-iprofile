# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.config import registry
from iprofile.core.utils import echo_red
import click
import sys


class IProfile(object):
    read_me = texts.IPROFILE_READ_ME.format(
        **{x: y.help for x, y in registry.get_all().iteritems()}
    )

    def __init__(self, argv, *args, **kwargs):
        if len(argv) == 1:
            click.echo(self.read_me)
            return
        name = argv.pop(1)
        command = registry.get_command(name)
        if not command:
            echo_red(texts.ERROR_COMMAND_NOT_FOUND.format(name))
            click.echo(self.read_me)
            return
        command()


def main():
    IProfile(argv=sys.argv)


if __name__ == '__main__':
    main()
