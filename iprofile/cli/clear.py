# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_ipython_name
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import list_profiles
import click
import os
import shutil


@icommand(help=texts.HELP_CLEAR, short_help=texts.HELP_CLEAR)
@click.argument('name', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
class Clear(ICommand):

    def run(self, **options):
        name = self.slugify_name(options)

        if not os.path.isdir(self.project_path):
            self.red(texts.ERROR_NO_PROFILES_TO_CLEAR)
            return []

        if not name:
            if options.get('no_input', False):
                return self.clear_all()
            if click.confirm(texts.INPUT_CONFIRM_DELETE):
                return self.clear_all()
            return []
        else:
            return self.run_for_profile(name)[0]

    def run_for_profile(self, name):
        ipython_path, _, _ = get_ipython_path(name)
        ipython_name = get_ipython_name(name)
        if not ipython_path:
            self.red(
                texts.ERROR_IPYTHON_PROFILE_DOESNT_EXIST.format(ipython_name))
            return name, False
        click.echo(
            texts.LOG_REMOVE_IPYTHON_PROFILE_ATTEMPT.format(ipython_path)
        )
        shutil.rmtree(ipython_path, ignore_errors=True)
        self.green(texts.LOG_REMOVE_IPYTHON_PROFILE.format(ipython_name))
        return name, True

    def clear_all(self):
        names = []
        cleared = 0
        for profile in list_profiles(self.project_path):
            name, result = self.run_for_profile(profile)
            names.append(name)
            if result:
                cleared += 1
        if cleared == 0:
            self.red(texts.ERROR_NO_PROFILES_TO_CLEAR)
        else:
            click.echo(texts.LOG_QTD_CLEARED.format(
                cleared, 's' if cleared != 1 else ''))
        return names
