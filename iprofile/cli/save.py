# -*- coding: utf-8 -*-

from glob2 import glob
from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import create_ipython_profile
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
import click
import os
import shutil


@icommand(help=texts.HELP_SAVE, short_help=texts.HELP_SAVE)
@click.argument('name')
@click.option('--no-symlink', is_flag=True, help=texts.HELP_NO_SYMLINKS)
class Save(ICommand):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(profile):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return

        create_ipython_profile(name)
        ipython_path, startup_path = get_ipython_path(name)
        abs_profile_path = os.path.abspath(profile)
        shutil.rmtree(startup_path, ignore_errors=True)

        if options.get('no_symlink', False):
            click.echo(texts.LOG_SAVING_PROFILE.format(ipython_path))
            shutil.copytree(abs_profile_path, startup_path)
        else:
            click.echo(texts.LOG_SAVING_SYMLINKS.format(ipython_path))
            os.makedirs(startup_path)
            files = glob('{}/**'.format(abs_profile_path))
            for file_path in files:
                os.symlink(file_path, '{}/{}'.format(
                    startup_path, os.path.basename(file_path)))
        self.green(texts.LOG_PROFILE_SAVED)
