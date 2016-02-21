# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.cli.active import CheckActiveMixin
from iprofile.core.models import ICommand


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
class Deactivate(CheckActiveMixin, ICommand):

    def run(self, **options):
        profile = self.check_active()
        if profile:
            profile.deactivate()
            self.green(texts.LOG_PROFILE_DEACTIVATED.format(profile.name))
