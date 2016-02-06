# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_ACTIVE, short_help=texts.HELP_ACTIVE)
class Active(ICommand):

    def run(self, **options):
        name = self.get_active_profile()
        (self.red(texts.ERROR_NO_ACTIVE_PROFILE) if not name else
         click.echo(texts.LOG_ACTIVE_PROFILE.format(name)))

    def get_active_profile(self):
        try:
            with open('{}/.active'.format(self.project_path), 'r') as active:
                return active.read()
        except IOError:
            return
