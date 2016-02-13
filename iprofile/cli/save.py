# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
from iprofile.core.utils import list_profiles
import click
import os
import shutil


@icommand(help=texts.HELP_SAVE, short_help=texts.HELP_SAVE)
@click.argument('name', required=False)
@click.option('--no-symlink', is_flag=True, help=texts.HELP_NO_SYMLINKS)
class Save(ICommand):

    def run(self, **options):
        name = options.get('name')
        if not name:
            for profile_name in list_profiles(
                    self.global_config.get('project_path')):
                profile = Profile(profile_name, self.global_config)
                self.run_for_profile(profile, **options)
        else:
            profile = Profile(name, self.global_config)
            self.run_for_profile(profile, **options)

    def run_for_profile(self, profile, **options):
        name = profile.name

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return

        profile.directory = profile.config.get('ipython_path')
        directory = profile.ipython_create()
        if directory and not profile.directory:
            profile.config.update({
                'ipython_path': directory
            }).save()

        self.save(profile, options.get('no_symlink', False))

    def save(self, profile, no_symlink):
        ipython = profile.path('ipython')
        files = {
            profile.path('config'): profile.path('ipython_config'),
            profile.path('startup'): profile.path('ipython_startup')
        }

        if no_symlink:
            click.echo(texts.LOG_SAVING_PROFILE.format(ipython))
        else:
            click.echo(texts.LOG_SAVING_SYMLINKS.format(ipython))

        for file_path, path_to_save in files.items():
            self.remove(path_to_save)
            if no_symlink:
                if os.path.isdir(file_path):
                    shutil.copytree(file_path, path_to_save)
                else:
                    shutil.copy(file_path, path_to_save)
            else:
                os.symlink(file_path, path_to_save)

        self.green(texts.LOG_PROFILE_SAVED)

    def remove(self, path):
        if os.path.islink(path):
            os.unlink(path)
        elif os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
