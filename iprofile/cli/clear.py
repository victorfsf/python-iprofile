# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
from iprofile.core.utils import list_profiles
import click
import shutil


@icommand(help=texts.HELP_CLEAR, short_help=texts.HELP_CLEAR)
@click.argument('name', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
class Clear(ICommand):

    def run(self, **options):
        profile = Profile(options.get('name'), self.global_config)

        if not profile.name:
            if options.get('no_input', False):
                return self.clear_all()
            if click.confirm(texts.INPUT_CONFIRM_DELETE):
                return self.clear_all()
            return []
        else:
            return self.run_for_profile(profile)[0]

    def run_for_profile(self, profile):
        ipython = profile.path('ipython')

        if not profile.ipython_exists():
            self.red(
                texts.ERROR_IPYTHON_PROFILE_DOESNT_EXIST.format(
                    profile.ipython_name))
            return profile.name, False
        click.echo(
            texts.LOG_REMOVE_IPYTHON_PROFILE_ATTEMPT.format(ipython)
        )
        shutil.rmtree(ipython, ignore_errors=True)
        self.green(
            texts.LOG_REMOVE_IPYTHON_PROFILE.format(profile.ipython_name))
        return profile.name, True

    def clear_all(self):
        names = []
        cleared = 0
        for profile in list_profiles(self.project_path):
            name, result = self.run_for_profile(
                Profile(profile, self.global_config)
            )
            names.append(name)
            if result:
                cleared += 1
        if cleared == 0:
            self.red(texts.ERROR_NO_PROFILES_TO_CLEAR)
        else:
            click.echo(texts.LOG_QTT_CLEARED.format(
                cleared, 's' if cleared != 1 else ''))
        return names
