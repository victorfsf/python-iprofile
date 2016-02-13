# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile import texts
import click


@icommand(help=texts.HELP_ACTIVE, short_help=texts.HELP_ACTIVE)
class Active(ICommand):

    def run(self, **options):
        name = self.global_config.get('active_profile')
        if not name:
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
        else:
            click.echo(texts.LOG_ACTIVE_PROFILE, nl=False)
            self.green(name)
