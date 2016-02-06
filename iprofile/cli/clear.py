# -*- coding: utf-8 -*-

from iprofile.core.decorators import icommand
from iprofile.core.mixins import ICommand
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_ipython_name
from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile import texts
import click
import shutil


@icommand(help=texts.HELP_CLEAR, short_help=texts.HELP_CLEAR)
@click.argument('name')
class Clear(ICommand):

    def run(self, **options):
        name = options.get('name')
        ipython_path, _ = get_ipython_path(name)
        ipython_name = get_ipython_name(name)

        if not ipython_path:
            echo_red(
                texts.ERROR_IPYTHON_PROFILE_DOESNT_EXIST.format(ipython_name))
            return name
        click.echo(
            texts.LOG_REMOVE_IPYTHON_PROFILE_ATTEMPT.format(ipython_path)
        )
        shutil.rmtree(ipython_path)
        echo_green(texts.LOG_REMOVE_IPYTHON_PROFILE.format(ipython_name))
        return name
