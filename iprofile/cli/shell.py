# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Create
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_ipython_name
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
from IPython import start_ipython
from slugify import slugify
import click
import os


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name', required=False)
class Shell(ICommand):

    def run(self, **options):
        if not options.get('name'):
            options['name'] = self.get_active_profile()
        name = options.get('name')

        if not name:
            start_ipython(argv=[])
            return

        ipython_name = get_ipython_name(name)
        ipython_path, _ = get_ipython_path(name)
        profile_path = get_profile_path(name)

        if profile_path and not os.path.isdir(profile_path):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_SHELL.format(name))
            Create.run(options)
            click.echo()
        elif not ipython_path:
            Save.run(options)
            click.echo()
        start_ipython(argv=['--profile', ipython_name])

    def get_active_profile(self):
        try:
            with open('{}/.active'.format(self.project_path), 'r') as active:
                return slugify(active.read().strip().replace('\n', ''))
        except IOError:
            return
