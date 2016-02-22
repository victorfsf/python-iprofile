# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_user_home
import click


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.option('--path', required=False, help=texts.HELP_INIT_PATH)
class Init(ICommand):

    settings_error = texts.ERROR_INIT_SETTINGS_EXIST

    def check_settings(self):
        if self.settings and self.settings.exists():
            return False
        return True

    def run(self, **options):
        path = options.get('path')

        self.settings.read(ignore_errors=True)
        if path:
            self.settings.update({
                'path': str(path)
            }).save()
            self.makedirs(get_user_home(path))
        self.green(
            texts.LOG_IPROFILE_INITIALIZED.format(
                path or 'iprofiles'
            )
        )
