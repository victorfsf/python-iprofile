# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import PROJECT_PATH
import click
import os
import shutil


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('name')
class Init(ICommand):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(PROJECT_PATH):
            os.makedirs(PROJECT_PATH)

        if os.path.isdir(profile):
            self.red(texts.ERROR_PROFILE_EXISTS.format(name))
            return

        startup = '{}/startup'.format(profile)
        if not self.check_ipython(name, profile, startup):
            os.makedirs(startup)
            startup_items = ['00_config.ipy', '01_imports.py']

            for item in startup_items:
                open('{}/{}'.format(startup, item), 'w').close()

            open('{}/ipython_config.py'.format(profile), 'w').close()

        with open('{}/README'.format(startup), 'w') as read_me:
            read_me.write(texts.IPYTHON_READ_ME.format(name))

        self.green(texts.LOG_NEW_PROFILE.format(name))
        click.echo(texts.LOG_PROFILE_PATH.format(profile))
        return profile

    def check_ipython(self, name, profile, startup):
        ipython_path, startup_path, config_file = get_ipython_path(name)

        if not ipython_path:
            return False

        if os.path.isdir(ipython_path) and os.path.isfile(config_file):
            os.makedirs(profile)
            shutil.copy(config_file, profile)

            if os.path.isdir(startup_path):
                shutil.copytree(startup_path, startup)
            return True
        return False
