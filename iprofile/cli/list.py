# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import list_profiles
import click


@icommand(help=texts.HELP_LIST, short_help=texts.HELP_LIST)
@click.option(
    '--show-only',
    type=click.Choice(['names', 'paths']),
    help=texts.HELP_SHOW_ONLY
)
class List(ICommand):

    def run(self, **options):
        try:
            profiles = list_profiles(self.project_path)
            qtd_profiles = len(profiles)
            if qtd_profiles == 0:
                self.no_profiles()
                return

            show_only = options.get('show_only', None)
            if not show_only:
                self.green(texts.LOG_QTD_PROFILES.format(
                    qtd_profiles,
                    's' if qtd_profiles != 1 else '',
                    'were' if qtd_profiles != 1 else 'was'
                ))

            for profile in profiles:
                if show_only == 'names':
                    click.echo(profile)
                elif show_only == 'paths':
                    click.echo(get_ipython_path(profile)[0])
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
