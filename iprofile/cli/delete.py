# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_profile_path
from iprofile.cli import Clear
from iprofile import texts
import click
import os
import shutil


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('name', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
class Delete(ICommand):

    def run(self, **options):
        name = Clear.run(options)
        if issubclass(name.__class__, list):
            deleted = 0
            for profile in name:
                result = self.run_for_profile(profile)
                if result:
                    deleted += 1
            if deleted == 0:
                self.red(texts.ERROR_NO_PROFILES_TO_DELETE)
            else:
                click.echo(texts.LOG_QTD_DELETED.format(
                    deleted, 's' if deleted != 1 else ''))
        elif name:
            self.run_for_profile(name)

    def run_for_profile(self, name):
        profile = get_profile_path(name)
        if not os.path.exists(profile):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
            return

        click.echo(texts.LOG_REMOVE_PROFILE_ATTEMPT.format(profile))
        shutil.rmtree(profile, ignore_errors=True)
        self.green(texts.LOG_REMOVE_PROFILE.format(name))
        return True
