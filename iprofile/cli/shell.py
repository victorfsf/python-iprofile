# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
import click
import IPython
import os


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('--django', required=False, help=texts.HELP_DJANGO)
@click.option('--settings', required=False, help=texts.HELP_DJANGO_SETTINGS)
class Shell(ICommand):

    def run(self, **options):
        profile = Profile(
            options.get('name') or self.get_active_profile() or '',
            self.global_config
        )
        ipython_options = list(options.get('ipython_options', []))
        # django_settings = options.get('django')
        # settings = options.get('settings')

        # if django_settings:
        #     import django
        #     if django_settings == '.':
        #         django_settings = get_django_settings_module()
        #     os.environ.setdefault(
        #         'DJANGO_SETTINGS_MODULE',
        #         '{0}.{1}'.format(django_settings, settings)
        #         if settings else django_settings
        #     )
        #     sys.path.append(os.path.abspath('.'))
        #     django.setup()
        # elif settings:
        #     self.red(texts.ERROR_SETTINGS_WITHOUT_DJANGO)
        #     return

        if not profile.name:
            IPython.start_ipython(argv=ipython_options)
            return

        ipython_path = profile.path('ipython')
        profile_path = profile.path('profile')

        if profile_path and not os.path.isdir(profile_path):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(profile.name))
            return

        if not ipython_path:
            Save.run(options)
            click.echo()
        IPython.start_ipython(
            argv=ipython_options + ['--profile-dir', ipython_path]
        )

    def get_active_profile(self):
        return self.global_config.get('active_profile')
