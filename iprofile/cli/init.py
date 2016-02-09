# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_user_home
from iprofile.core.utils import PROJECT_PATH
import click
import os
import shutil


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('name')
@click.option('--profile-dir', required=False, help=texts.HELP_PROFILE_DIR)
class Init(ICommand):

    def run(self, **options):
        name = options.get('name')
        profile_dir = options.get('profile_dir')
        profile = get_profile_path(name)

        if not self.check_directories(profile, name):
            return

        startup = '{0}/startup'.format(profile)
        if not self.check_ipython(name, profile, startup, profile_dir):
            self.create_profile(profile, startup, profile_dir)

        with open('{0}/README'.format(startup), 'w') as read_me:
            read_me.write(texts.IPYTHON_READ_ME.format(name))

        self.green(texts.LOG_NEW_PROFILE.format(name))
        click.echo(texts.LOG_PROFILE_PATH.format(profile))
        return profile

    def check_ipython(self, name, profile, startup, directory):
        ipython_path, startup_path, config_file = get_ipython_path(
            name, directory)

        if not ipython_path:
            return False

        if os.path.isdir(ipython_path) and os.path.isfile(config_file):
            os.makedirs(profile)
            shutil.copy(config_file, profile)

            if os.path.isdir(startup_path):
                shutil.copytree(startup_path, startup)
            return True
        return False

    def check_directories(self, profile, name):
        if not os.path.isdir(PROJECT_PATH):
            os.makedirs(PROJECT_PATH)

        if os.path.isdir(profile):
            self.red(texts.ERROR_PROFILE_EXISTS.format(name))
            return False

        return True

    def create_profile(self, profile, startup, directory):
        os.makedirs(startup)

        for item in ['00_config.ipy', '01_imports.py']:
            open('{0}/{1}'.format(startup, item), 'w').close()

        open('{0}/ipython_config.py'.format(profile), 'w').close()
        self.create_config(profile, directory)

    def create_config(self, profile, directory):
        profile_config = '{0}/.config'.format(profile)
        if os.path.isfile(profile_config):
            with open(profile_config, 'r') as f:
                config_data = f.readlines()
        elif directory and profile not in os.path.abspath(
                get_user_home(directory)):
            config_data = ['PROFILE_DIR={0}'.format(directory)]
        else:
            config_data = []

        with open(profile_config, 'w') as f:
            for data in config_data:
                f.write(data)
