# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.cli.add import Add
from iprofile.cli.save import Save
from iprofile.models import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_CREATE, short_help=texts.HELP_CREATE)
@click.argument('name')
@click.option('--no-symlink', is_flag=True, help=texts.HELP_NO_SYMLINKS)
@click.option(
    '--profile-dir',
    required=False,
    help=texts.HELP_PROFILE_DIR,
    type=click.Path()
)
class Create(ICommand):

    def run(self, **options):
        if Add.run(options):
            Save.run(options)
