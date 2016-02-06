# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.mixins import ActivateDeactivateMixin
from iprofile.core.decorators import icommand
import click
import os


@icommand(help=texts.HELP_DEACTIVATE, short_help=texts.HELP_DEACTIVATE)
@click.argument('name')
class Deactivate(ActivateDeactivateMixin):

    def run(self, **options):
        name = super(Deactivate.callback, self).run(**options)
        if name:
            self.deactivate_profile(name)

    def deactivate_profile(self, profile_name):
        active_path = '{}/.active'.format(self.project_path)
        try:
            with open(active_path, 'r') as active:
                active_profile = active.read()
            if active_profile != profile_name:
                self.red(texts.ERROR_PROFILE_NOT_ACTIVE.format(profile_name))
                return
            os.remove(active_path)
            self.green(texts.LOG_PROFILE_DEACTIVATED.format(profile_name))
        except IOError:
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
