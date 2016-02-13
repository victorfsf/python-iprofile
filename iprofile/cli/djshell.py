# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.shell import Shell
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
import click
import os
import sys


@icommand(help=texts.HELP_DJANGO, short_help=texts.HELP_DJANGO)
@click.argument('name', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option(
    '--settings', required=False,
    help=texts.HELP_SETTINGS, short_help=texts.HELP_SETTINGS
)
class Django(ICommand):

    def run(self, **options):
        import django

        settings = (
            options.get('settings') or
            self.global_config.get('django_settings_module')
        )

        if not settings:
            self.red(texts.ERROR_DJANGO_WITHOUT_SETTINGS)
            return

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
        sys.path.append(os.getcwd())
        try:
            django.setup()
        except ImportError:
            self.red(texts.ERROR_DJANGO_INVALID_SETTINGS.format(settings))
            return

        Shell.run(options)
