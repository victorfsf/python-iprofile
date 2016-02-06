# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.models import ICommand
from iprofile.core.decorators import icommand
import os


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
class Deactivate(ICommand):

    def run(self, **options):
        active_path = '{}/.active'.format(self.project_path)
        try:
            os.remove(active_path)
        except (IOError, OSError):
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
