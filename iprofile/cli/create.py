# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.cli.init import Init
from iprofile.cli.save import Save
from iprofile.core.models import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_CREATE, short_help=texts.HELP_CREATE)
@click.argument('name')
@click.option('--no-symlink', is_flag=True, help=texts.HELP_NO_SYMLINKS)
class Create(ICommand):

    def run(self, **options):
        profile = Init.run(options)
        if profile:
            Save.run(options)
