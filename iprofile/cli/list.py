# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.utils import list_profiles
import click


@icommand(help=texts.HELP_LIST, short_help=texts.HELP_LIST)
@click.option('--names-only', is_flag=True, help=texts.HELP_NAMES_ONLY)
class List(ICommand):

    def run(self, **options):
        profiles_path = self.settings.get('path')
        profiles_list = list_profiles(profiles_path)

        if not profiles_list:
            self.red(texts.ERROR_NO_PROFILES_TO_LIST)
            return

        active = self.settings.get('active')
        qtt_profiles = len(profiles_list)
        qtt_text = texts.LOG_QTT_PROFILES.format(
            qtt_profiles,
            's' if qtt_profiles > 1 else '',
            'were' if qtt_profiles > 1 else 'was'
        )

        if not options.get('names_only'):
            self.green(qtt_text)

        for profile in profiles_list:
            if active == profile:
                self.pgreen(profile)
            else:
                click.echo(profile)
