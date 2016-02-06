# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import Command
import click


@icommand()
@click.argument('name', metavar='<profile name>', required=False)
class Help(Command):

    def run(self, **options):
        pass
