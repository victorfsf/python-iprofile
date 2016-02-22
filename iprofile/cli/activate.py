# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_ACTIVATE, short_help=texts.HELP_ACTIVATE)
@click.argument('profile')
class Activate(ICommand):

    def run(self, **options):
        name = slugify(options.get('profile'))

        if not name:
            self.red(texts.ERROR_PROFILE_INVALID_NAME.format(
                options.get('profile')
            ))
            return

        profile = Profile(name)

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
            return

        profile.activate()
        self.green(texts.LOG_PROFILE_ACTIVATED.format(name))
