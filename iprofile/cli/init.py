# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
import click
import os


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('path', required=False)
class Init(ICommand):

    def run(self, **options):
        path = options.get('path') or 'iprofiles'

        try:
            abspath = os.path.abspath(os.path.join(os.getcwd(), path))
            os.makedirs(abspath)

            if self.project_path != path:
                action = 'Changed'
            else:
                action = 'Created'

            self.global_config.update({
                'project_path': '{0}/'.format(path)
            }).save()
            self.green(texts.LOG_IPROFILE_INITIALIZED.format(abspath))
            click.echo(texts.LOG_IPROFILE_YML.format(os.getcwd(), action))
        except OSError:
            self.red(texts.ERROR_INIT_PATH_EXISTS.format(abspath))
