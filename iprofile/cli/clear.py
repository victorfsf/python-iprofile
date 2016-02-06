# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_CLEAR, short_help=texts.HELP_CLEAR)
@click.argument('name')
class Clear(ICommand):

    def run(self, **options):
        pass
