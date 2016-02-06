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

        if not self.check_ipython(name, profile):
            os.makedirs(profile)
            profile_items = ['00_config.ipy', '01_imports.py']
            for item in profile_items:
                open('{}/{}'.format(profile, item), 'w').close()

        with open('{}/README'.format(profile), 'w') as read_me:
            read_me.write(texts.IPYTHON_READ_ME.format(name))

        self.green(texts.LOG_NEW_PROFILE.format(name))
        click.echo(texts.LOG_PROFILE_PATH.format(profile))
        return profile

    def check_ipython(self, name, profile):
        _, startup_path = get_ipython_path(name)
        ipython_files = os.listdir(startup_path) if startup_path else []
        if 'README' in ipython_files:
            ipython_files.remove('README')

        if startup_path and os.path.isdir(startup_path) and ipython_files:
            shutil.copytree(startup_path, profile)
            shutil.rmtree(startup_path, ignore_errors=True)
            return True
        return False
