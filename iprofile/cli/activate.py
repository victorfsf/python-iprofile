# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_profile_path
import click
import os


@icommand(help=texts.HELP_ACTIVATE, short_help=texts.HELP_ACTIVATE)
@click.argument('name')
class Activate(ICommand):

    def run(self, **options):
        name = self.slugify_name(options)
        profile = get_profile_path(name)

        if not os.path.isdir(profile):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return

        self.activate_profile(name)
        self.green(texts.LOG_PROFILE_ACTIVATED.format(name))

    def activate_profile(self, profile_name):
        with open('{0}/.active'.format(self.project_path), 'w') as active:
            active.write(profile_name)
