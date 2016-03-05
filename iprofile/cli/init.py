# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli.activate import Activate
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_user_home
from iprofile.profiles.models import Profile
import click


@icommand(help=texts.HELP_INIT, short_help=texts.HELP_INIT)
@click.option('--path', required=False, help=texts.HELP_INIT_PATH)
@click.option('--active', required=False, help=texts.HELP_INIT_ACTIVE)
class Init(ICommand):

    settings_error = texts.ERROR_INIT_SETTINGS_EXIST

    def check_settings(self):
        if self.settings and self.settings.exists():
            return False
        return True

    def run(self, **options):
        path = options.get('path')
        active = options.get('active')

        self.settings.read(ignore_errors=True)
        if path:
            self.settings.update({
                'path': str(path)
            }).save()
            self.makedirs(get_user_home(path))
        self.green(
            texts.LOG_IPROFILE_INITIALIZED.format(
                path or 'iprofiles'
            )
        )
        if active:
            if not Profile(active).exists():
                self.red(texts.ERROR_PROFILE_DOESNT_EXIST.format(active))
                return
            self.activate(path or 'iprofiles', active)
        else:
            self.activate(path or 'iprofiles')

    def activate(self, path, profile=None):
        if self.isdir(path):
            if profile:
                Activate.run({'profile': profile})
            else:
                profiles = self.list_profiles(path)
                if len(profiles) == 1:
                    Activate.run({'profile': profiles[0]})
