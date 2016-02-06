# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile.core.utils import get_profile_path
from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile.cli import Clear
from iprofile import texts
import click
import os
import shutil


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('name')
class Delete(ICommand):

    def run(self, **options):
        name = Clear.run(options)
        profile = get_profile_path(name)

        if not os.path.exists(profile):
            echo_red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
            return

        click.echo(texts.LOG_REMOVE_PROFILE_ATTEMPT.format(profile))
        shutil.rmtree(profile)
        echo_green(texts.LOG_REMOVE_PROFILE.format(name))
