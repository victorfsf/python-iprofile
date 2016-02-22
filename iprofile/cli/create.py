# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from iprofile.profiles.utils import list_profiles
from slugify import slugify
import click


@icommand(help=texts.HELP_CREATE, short_help=texts.HELP_CREATE)
@click.argument('profile')
@click.option('--active', is_flag=True, help=texts.HELP_CREATE_ACTIVE)
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

        all_profiles = list_profiles(self.settings.get('path'))
        profile.create()
        self.green(texts.LOG_NEW_PROFILE.format(name))

        if options.get('active') or not all_profiles:
            profile.activate()
            self.green(texts.LOG_PROFILE_ACTIVATED.format(name))
