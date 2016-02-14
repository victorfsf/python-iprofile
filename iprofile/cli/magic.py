# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.utils import makedirs
from iprofile.models import ICommand
from iprofile.models import Profile
from iprofile.scripts import ipython
from glob import glob
import click
import os


@icommand(help=texts.HELP_MAGIC, short_help=texts.HELP_MAGIC)
@click.argument('profile')
@click.argument('script')
@click.argument('filename', required=False)
class Magic(ICommand):

    def run(self, **options):
        script_name = options.get('script')
        ipython_script = getattr(ipython, script_name, None)

        if not ipython_script:
            self.red(
                texts.ERROR_IPYTHON_SCRIPT_DOESNT_EXIST.format(script_name))
            return

        filename = options.get('filename')
        profile = Profile(
            self.get_active_profile(options.get('profile')), self.global_config
        )

        if not profile.name:
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return

        if not profile.exists():
            self.red(
                texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(profile.name)
            )
            return

        makedirs(profile.path('startup'))
        if not filename:
            pathlist = glob(os.path.join(profile.path('startup'), '*.ipy'))
            if not pathlist:
                path = os.path.join(
                    profile.path('startup'), '00_{0}.ipy'.format(script_name)
                )
            else:
                path = pathlist[0]
        else:
            path = os.path.join(
                profile.path('startup'), '{0}.ipy'.format(filename)
            )

        with open(path, 'a') as f:
            f.write(ipython_script)

        self.green(texts.LOG_IPYTHON_SCRIPT_ADDED.format(script_name))
        click.echo(path)
