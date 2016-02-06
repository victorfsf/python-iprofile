# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.cli.init import Init
from iprofile.cli.save import Save
from iprofile.core.mixins import Command
from iprofile import texts
import click


@icommand(help=texts.HELP_CREATE)
@click.argument('name', metavar='<profile name>')
@click.option('--no-symlink', is_flag=True, help=texts.HELP_NO_SYMLINKS)
class Create(Command):

    def run(self, **options):
        profile = Init.callback(_auto_run=False).run(**options)
        if profile:
            Save()
