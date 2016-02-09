# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.models import ICommand
from iprofile.core.decorators import icommand
import os


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
class Deactivate(ICommand):

    def run(self, **options):
        active_path = '{0}/.active'.format(self.project_path)
        try:
            with open(active_path, 'r') as active:
                name = active.read()
            os.remove(active_path)
            self.green(texts.LOG_PROFILE_DEACTIVATED.format(name))
        except (IOError, OSError):
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
