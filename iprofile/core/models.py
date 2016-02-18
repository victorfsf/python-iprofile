# -*- coding: utf-8 -*-

from iprofile.core.utils import echo_green
from iprofile.core.utils import echo_red
from iprofile.settings.models import GlobalSettings
from iprofile.settings.models import ProfileSettings
import click


class ICommand(object):

    def __init__(self, _autorun=True, *args, **kwargs):
        self.settings = GlobalSettings()
        self.profile = ProfileSettings(self.settings, kwargs.get('profile'))

        if _autorun:
            self.run(**kwargs.copy())
        kwargs.clear()

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
