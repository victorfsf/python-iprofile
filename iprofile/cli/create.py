# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_CREATE, short_help=texts.HELP_CREATE)
@click.argument('profile')
@click.option('--active', is_flag=True, help=texts.HELP_CREATE_ACTIVE)
@click.option('-p', '--project', required=False, help=texts.HELP_PROJECT_OPT)
@click.option('--no-ignore', is_flag=True, help=texts.HELP_NO_IGNORE)
class Create(ICommand):

    def run(self, **options):
        name = slugify(options.get('profile'))
        project = options.get('project')
        no_ignore = options.get('no_ignore')

        if not name:
            self.red(texts.ERROR_PROFILE_INVALID_NAME.format(
                options.get('profile')
            ))
            return

        profile = Profile(name, project=project, ignore_project=no_ignore)

        if profile.exists():
            self.red(texts.ERROR_PROFILE_EXISTS.format(name))
            return

        all_profiles = self.list_profiles(self.settings.get('path'))
        profile.create()
        self.green(texts.LOG_NEW_PROFILE.format(name))

        if options.get('active') or not all_profiles:
            profile.activate()
            self.green(texts.LOG_PROFILE_ACTIVATED.format(name))
