# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.models import ICommand
from iprofile.models import Profile
import click


@icommand(help=texts.HELP_CONFIG, short_help=texts.HELP_CONFIG)
@click.argument('name')
@click.argument('value')
@click.option('--profile', required=False, help=texts.HELP_CONFIG_PROFILE)
class Config(ICommand):

    shortcuts = {
        'django': 'django_settings_module'
    }

    def run(self, **options):
        value = options.get('value')
        name = options.get('name').strip()
        profile_name = options.get('profile')
        config_dict = {
            str(self.shortcuts.get(name, name)): str(value)
        }

        if profile_name:
            profile = Profile(profile_name, self.global_config)
            profile.config.update(config_dict).save()
        else:
            self.global_config.update(config_dict).save()
