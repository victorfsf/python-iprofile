# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_CREATE, short_help=texts.HELP_CREATE)
@click.argument('profile')
class Create(ICommand):

    def run(self, **options):
        name = slugify(options.get('profile'))

        if not name:
            self.red(texts.ERROR_PROFILE_INVALID_NAME.format(
                options.get('profile')
            ))
            return

        profile = Profile(name)

        if profile.exists():
            self.red(texts.ERROR_PROFILE_EXISTS.format(name))
            return

        profile.create()
        self.green(texts.LOG_NEW_PROFILE.format(name))
