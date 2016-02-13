# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
import click


@icommand(help=texts.HELP_CONFIG, short_help=texts.HELP_CONFIG)
@click.argument('name')
@click.argument('value')
class Config(ICommand):

    shortcuts = {
        'django': 'django_settings_module'
    }

    def run(self, **options):
        value = options.get('value')
        name = options.get('name').strip()

        self.global_config.update({
            str(self.shortcuts.get(name, name)): str(value)
        }).save()
