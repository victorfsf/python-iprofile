# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


class CheckActiveMixin(object):

    def check_active(self):
        name = self.settings.get('active')
        project = None

        if not name or not slugify(name):
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return

        if ':' in name:
            name, project = name.split(':')

        profile = Profile(name, project=project)
        if not profile.exists():
            self.settings.update({
                'active': None
            }).save()
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return
        return profile


@icommand(help=texts.HELP_ACTIVE, short_help=texts.HELP_ACTIVE)
class Active(CheckActiveMixin, ICommand):

    def run(self, **options):
        profile = self.check_active()
        if profile:
            click.echo(texts.LOG_ACTIVE_PROFILE, nl=False)
            self.pgreen(profile.name)
