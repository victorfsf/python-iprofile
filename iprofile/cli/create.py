# -*- coding: utf-8 -*-

from iprofile.core.decorators import iregister
from iprofile.cli.init import Init
from iprofile.cli.save import Save
from iprofile.core.mixins import Command
import click


@iregister
@click.command()
@click.argument('name')
@click.option('--no-symlink', is_flag=True)
class Create(Command):

    def run(self, **options):
        profile = Init.callback(_auto_run=False).run(**options)
        if profile:
            Save()
