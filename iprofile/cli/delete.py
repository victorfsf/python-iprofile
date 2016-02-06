# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('name')
class Delete(ICommand):

    def run(self, **options):
        pass
