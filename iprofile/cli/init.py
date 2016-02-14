# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.utils import GLOBAL_SETTINGS_FILE
from iprofile.models import ICommand
from slugify import slugify
import click
import os


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('path', required=False)
@click.option('--name', required=False, help=texts.HELP_NAME_INIT)
class Init(ICommand):

    def run(self, **options):
        path = options.get('path') or 'iprofiles'
        name = slugify(options.get('name', ''))

        try:
            abspath = os.path.abspath(os.path.join(os.getcwd(), path))
            os.makedirs(abspath)

            if self.project_path != path:
                action = 'Changed'
            else:
                action = 'Created'

            self.global_config.update({
                'project_path': '{0}/'.format(path),
            })
            if name:
                self.global_config.update({
                    'project_name': name
                })
            self.global_config.save()

            self.green(texts.LOG_IPROFILE_INITIALIZED.format(abspath))
            click.echo(texts.LOG_IPROFILE_YML.format(
                os.getcwd(), action, GLOBAL_SETTINGS_FILE))

        except OSError:
            self.red(texts.ERROR_INIT_PATH_EXISTS.format(abspath))
