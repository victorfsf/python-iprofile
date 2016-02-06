# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import Command
from iprofile.core.utils import PROJECT_PATH
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile.cli import texts
import click
import os


@icommand()
@click.argument('name', metavar='<profile name>')
class Init(Command):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(PROJECT_PATH):
            os.makedirs(PROJECT_PATH)

        if os.path.isdir(profile):
            echo_red(texts.ERROR_PROFILE_EXISTS.format(name))
            return

        os.makedirs(profile)
        profile_items = ['00.ipy', '01.py']
        for item in profile_items:
            open('{}/{}'.format(profile, item), 'w').close()
        with open('{}/README'.format(profile), 'w') as read_me:
            read_me.write(texts.IPYTHON_READ_ME)

        click.echo(texts.LOG_PROFILE_PATH.format(profile))
        echo_green(texts.LOG_NEW_PROFILE.format(name))
        return profile
