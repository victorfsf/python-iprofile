# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.models import ICommand
from iprofile.core.decorators import icommand


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
class Deactivate(ICommand):

    def run(self, **options):
        name = self.global_config.pop('active_profile')

        if not name:
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return

        self.global_config.save()
        self.green(texts.LOG_PROFILE_DEACTIVATED.format(name))
