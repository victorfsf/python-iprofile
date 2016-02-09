# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
import click
import os


@icommand(help=texts.HELP_LIST, short_help=texts.HELP_LIST)
@click.option('--name-only', is_flag=True, help=texts.HELP_NAME_ONLY)
class List(ICommand):

    def run(self, **options):
        try:
            profiles = filter(
                lambda x: os.path.isdir('{0}/{1}'.format(self.project_path, x))
                and 'ipython_config.py' in os.listdir('{0}/{1}'.format(
                    self.project_path, x)), os.listdir('iprofiles'))

            if len(profiles) == 0:
                self.no_profiles()
                return

            name_only = options.get('name_only', False)
            if not name_only:
                self.green(texts.LOG_QTD_PROFILES.format(len(profiles)))

            for profile in profiles:
                if name_only:
                    click.echo(profile)
                else:
                    ipython_path, _, _ = get_ipython_path(profile)
                    click.echo('\nName: {}'.format(profile))
                    click.echo('IPython profile path:\t{}'.format(
                        ipython_path))
                    click.echo('Project profile path:\t{}'.format(
                        get_profile_path(profile)))
        except OSError:
            self.no_profiles()

    def no_profiles(self):
        self.red(texts.ERROR_NO_PROFILES_TO_LIST)
