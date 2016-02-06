# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Create
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile.core.utils import echo_red
from iprofile.core.utils import get_ipython_name
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
from IPython import start_ipython
import click
import os


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name')
class Shell(ICommand):

    def run(self, **options):
        name = options.get('name')
        ipython_name = get_ipython_name(name)
        ipython_path, _ = get_ipython_path(name)
        profile_path = get_profile_path(name)

        if profile_path and not os.path.isdir(profile_path):
            echo_red(texts.ERROR_PROFILE_DOESNT_EXIST_SHELL.format(name))
            Create.run(options)
            click.echo()
        elif not ipython_path:
            Save.run(options)
            click.echo()
        start_ipython(argv=['--profile', ipython_name])
