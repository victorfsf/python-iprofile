# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
import click
import os


@icommand(help=texts.HELP_ACTIVATE, short_help=texts.HELP_ACTIVATE)
@click.argument('name')
class Activate(ICommand):

    def run(self, **options):
        profile = Profile(options.get('name'), self.global_config)
        name = profile.name

        if not os.path.isdir(profile.path('profile')):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return

        self.activate_profile(name)
        self.green(texts.LOG_PROFILE_ACTIVATED.format(name))

    def activate_profile(self, profile_name):
        self.global_config.update({
            'active_profile': profile_name
        }).save()
