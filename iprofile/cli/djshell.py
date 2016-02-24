# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.shell import Shell
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
import click
import os
import sys
import traceback
import six


@icommand(help=texts.HELP_DJANGO, short_help=texts.HELP_DJANGO)
@click.argument('profile', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('--settings', required=False, help=texts.HELP_SETTINGS)
class Django(ICommand):

    def run(self, **options):
        try:
            import django
        except ImportError:
            self.red(texts.ERROR_DJANGO_NOT_INSTALLED)
            return

        settings = (
            options.get('settings') or
            self.settings.get('django')
        )

        if not (settings and isinstance(settings, six.string_types)):
            self.red(texts.ERROR_DJANGO_WITHOUT_SETTINGS)
            return

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
        sys.path.append(os.getcwd())
        try:
            django.setup()
        except Exception:
            self.red(texts.ERROR_DJANGO_INVALID_SETTINGS.format(settings))
            traceback.print_exc()
            return

        Shell.run(options)
