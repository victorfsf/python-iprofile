# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
import click
import IPython
import os


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('--django', required=False, help=texts.HELP_DJANGO)
class Shell(ICommand):

    def run(self, **options):
        profile = Profile(
            self.get_active_profile(options.get('name')), self.global_config
        )

        ipython_options = list(options.get('ipython_options', []))

        if not profile.name:
            IPython.start_ipython(argv=ipython_options)
            return

        profile_path = profile.path('profile')
        ipython_path = profile.path('ipython')

        if profile_path and not os.path.isdir(profile_path):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(profile.name))
            return

        if not (ipython_path and os.path.isdir(ipython_path)):
            Save.run(options)
            profile.ipython_locate()
            ipython_path = profile.path('ipython')
            click.echo()

        IPython.start_ipython(
            argv=ipython_options + ['--profile-dir', ipython_path]
        )

    def get_active_profile(self, name):
        if not name or name == '.':
            return self.global_config.get('active_profile')
        return name
