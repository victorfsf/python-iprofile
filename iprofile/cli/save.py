# -*- coding: utf-8 -*-

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
        ipython_path, startup_path, config_file = get_ipython_path(name)
        abs_profile_path = os.path.abspath(profile)

        files = [
            '{}/ipython_config.py'.format(abs_profile_path),
            '{}/startup'.format(abs_profile_path)
        ]
        self.save(ipython_path, files, options.get('no_symlink', False))

    def save(self, ipython_path, files, no_symlinks):
        if no_symlinks:
            click.echo(texts.LOG_SAVING_PROFILE.format(ipython_path))
        else:
            click.echo(texts.LOG_SAVING_SYMLINKS.format(ipython_path))

        for file_path in files:
            path_to_save = '{}/{}'.format(
                ipython_path, os.path.basename(file_path))
            self.remove(path_to_save)
            if no_symlinks:
                if os.path.isdir(file_path):
                    shutil.copytree(file_path, path_to_save)
                else:
                    shutil.copy(file_path, path_to_save)
            else:
                os.symlink(file_path, path_to_save)

        self.green(texts.LOG_PROFILE_SAVED)

    def remove(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        if os.path.islink(path):
            os.unlink(path)
        if os.path.isfile(path):
            os.remove(path)
