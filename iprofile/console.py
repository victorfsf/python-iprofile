# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.config import registry
import click


class IProfile(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(registry.get_all())

    def get_command(self, ctx, name):
        command = registry.get_command(name)
        return command


@click.command(
    cls=IProfile,
    help=texts.IPROFILE_READ_ME
)
@click.version_option(version='0.1.1b', prog_name="IProfile")
def main():
    pass
