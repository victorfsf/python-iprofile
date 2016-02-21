# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.shell import Shell
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
import click
import os
import sys
import traceback


@icommand(help=texts.HELP_DJANGO, short_help=texts.HELP_DJANGO)
@click.argument('profile', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('--default', is_flag=True, help=texts.HELP_SHELL_DEFAULT)
@click.option('--settings', required=False, help=texts.HELP_SETTINGS)
class Django(ICommand):

    def run(self, **options):
        import django

        settings = (
            options.get('settings') or
            self.settings.get('django')
        )

        if not settings or not isinstance(settings, basestring):
            self.red(texts.ERROR_DJANGO_WITHOUT_SETTINGS)
            return

        self.settings.update({
            'django': settings
        }).save()

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
        sys.path.append(os.getcwd())
        try:
            django.setup()
        except:
            self.red(texts.ERROR_DJANGO_INVALID_SETTINGS.format(settings))
            traceback.print_exc()
            return

        Shell.run(options)
