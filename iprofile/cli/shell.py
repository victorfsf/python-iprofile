# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_active_profile
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
import click
import IPython
import os


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name', required=False, default=get_active_profile())
class Shell(ICommand):

    def run(self, **options):
        name = options.get('name')

        if not name:
            IPython.start_ipython(argv=[])
            return

        ipython_path, _, _ = get_ipython_path(name)
        profile_path = get_profile_path(name)

        if profile_path and not os.path.isdir(profile_path):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return
        elif not ipython_path:
            Save.run(options)
            click.echo()
        IPython.start_ipython(argv=['--profile-dir', ipython_path])
