# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
import ast
import click
import re


@icommand(help=texts.HELP_CONFIG, short_help=texts.HELP_CONFIG)
@click.argument('name')
@click.argument('value')
class Config(ICommand):

    def run(self, **options):
        name = options.get('name').strip()
        value = str(options.get('value').strip())

        if re.match(r'^\{.*\}$', value) or re.match(r'^\[.*\]$', value):
            value = ast.literal_eval(value)

        self.settings.update({
            str(name): value
        }).save()
