# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.utils import makedirs
from iprofile.models import ICommand
from iprofile.models import Profile
import click
import os


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.argument('name')
@click.option(
    '--profile-dir',
    required=False,
    help=texts.HELP_PROFILE_DIR,
    type=click.Path()
)
@click.option('--autoreload', is_flag=True)
class Add(ICommand):

    def run(self, **options):
        profile = Profile(
            options.get('name'),
            self.global_config,
            directory=options.get('profile_dir')
        )

        if not self.check_directories(profile):
            return

        self.create_profile(profile, options.get('autoreload'))

        if profile.directory:
            profile.config.update({
                'ipython_path': profile.directory
            }).save()
        else:
            profile.config.save()

        with open(os.path.join(profile.path('startup'), 'README'), 'w') as f:
            f.write(texts.IPYTHON_READ_ME.format(profile.name))

        self.green(texts.LOG_NEW_PROFILE.format(profile.name))
        click.echo(texts.LOG_PROFILE_PATH.format(profile.path('profile')))
        return True

    def check_directories(self, profile):
        makedirs(self.project_path)

        if profile.exists():
            self.red(texts.ERROR_PROFILE_EXISTS.format(profile.name))
            return False

        return True

    def create_profile(self, profile, autoreload):
        startup = profile.path('startup')
        makedirs(startup)
        if autoreload:
            with open(os.path.join(startup, '00_autoreload.ipy'), 'w') as f:
                f.write('%load_ext autoreload\n%autoreload 2\n')
            open(os.path.join(startup, '01_imports.py'), 'w').close()
        else:
            for item in ['00_config.ipy', '01_imports.py']:
                open(os.path.join(startup, item), 'w').close()

        open(profile.path('config'), 'w').close()
