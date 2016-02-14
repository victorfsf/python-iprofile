# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
from iprofile.cli import Clear
from iprofile import texts
import click
import shutil


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('name', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
class Delete(ICommand):

    def run(self, **options):
        names = Clear.run(options)
        if issubclass(names.__class__, list):
            deleted = 0
            for profile_name in names:
                profile = Profile(profile_name, self.global_config)
                result = self.run_for_profile(profile)
                if result:
                    deleted += 1
            if deleted == 0:
                self.red(texts.ERROR_NO_PROFILES_TO_DELETE)
            else:
                click.echo(texts.LOG_QTT_DELETED.format(
                    deleted, 's' if deleted != 1 else ''))
        elif names:
            self.run_for_profile(Profile(names, self.global_config))

    def run_for_profile(self, profile):
        name = profile.name
        profile_path = profile.path('profile')

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
            return

        click.echo(texts.LOG_REMOVE_PROFILE_ATTEMPT.format(profile_path))
        shutil.rmtree(profile_path, ignore_errors=True)
        self.green(texts.LOG_REMOVE_PROFILE.format(name))
        return True
