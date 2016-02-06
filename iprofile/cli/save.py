# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import Command
from iprofile.core.utils import create_ipython_profile
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import echo_green
from iprofile.core.utils import echo_red
from iprofile.cli import texts
from glob2 import glob
import click
import os
import shutil


@icommand()
@click.argument('name', metavar='<profile name>')
@click.option('--no-symlink', is_flag=True)
class Save(Command):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(profile):
            echo_red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
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
        echo_green(texts.LOG_PROFILE_SAVED)
