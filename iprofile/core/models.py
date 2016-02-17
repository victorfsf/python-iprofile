# -*- coding: utf-8 -*-

from iprofile.core.utils import echo_green
from iprofile.core.utils import echo_red
from iprofile.settings.utils import GLOBAL_SETTINGS_FILE
from iprofile.settings.utils import PROFILE_SETTINGS_FILE
from iprofile.settings.models import Settings
import click


class ICommand(object):

    def __init__(self, _autorun=True, *args, **kwargs):
        self.profile = Settings(PROFILE_SETTINGS_FILE)
        self.settings = Settings(GLOBAL_SETTINGS_FILE)

        if _autorun:
            self.run(**kwargs.copy())
        kwargs = {}
        super(ICommand, self).__init__(*args, **kwargs)

    def run(self, **options):
        raise NotImplementedError

    def red(self, text):
        return echo_red(text)

    def green(self, text):
        return echo_green(text)


class Command(click.Command):

    def run(self, options):
        return (
            self.callback(_autorun=False).run(**options)
            if self.callback else None
        )
