# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile.core.utils import echo_green
from iprofile.core.utils import echo_red
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import PROJECT_PATH
import click
import os


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('name')
class Init(ICommand):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(PROJECT_PATH):
            os.makedirs(PROJECT_PATH)

        if os.path.isdir(profile):
            echo_red(texts.ERROR_PROFILE_EXISTS.format(name))
            return

        os.makedirs(profile)
        profile_items = ['00_config.ipy', '01_imports.py']
        for item in profile_items:
            open('{}/{}'.format(profile, item), 'w').close()

        with open('{}/README'.format(profile), 'w') as read_me:
            read_me.write(texts.IPYTHON_READ_ME.format(name))

        echo_green(texts.LOG_NEW_PROFILE.format(name))
        click.echo(texts.LOG_PROFILE_PATH.format(profile))
        return profile
