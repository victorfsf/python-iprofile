# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.mixins import ActivateDeactivateMixin
from iprofile.core.decorators import icommand
import click


@icommand(help=texts.HELP_ACTIVATE, short_help=texts.HELP_ACTIVATE)
@click.argument('name')
class Activate(ActivateDeactivateMixin):

    def run(self, **options):
        name = super(Activate.callback, self).run(**options)
        if name:
            self.activate_profile(name)
            self.green(texts.LOG_PROFILE_ACTIVATED.format(name))

    def activate_profile(self, profile_name):
        with open('{}/.active'.format(self.project_path), 'w') as active:
            active.write(profile_name)
