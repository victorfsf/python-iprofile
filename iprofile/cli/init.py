# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
import click


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('path', required=False)
class Init(ICommand):

    settings_error = texts.ERROR_INIT_SETTINGS_EXIST

    def check_settings(self):
        if self.settings:
            return False
        return True

    def run(self, **options):
        path = options.get('path')

        self.settings.read(ignore_errors=True)
        if path:
            self.settings.get('profiles').update({
                'path': str(path)
            }).save()
