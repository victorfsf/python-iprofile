# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
@click.argument('name')
class Deactivate(ICommand):

    def run(self, **options):
        pass
