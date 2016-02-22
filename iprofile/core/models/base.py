# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.utils import echo_green
from iprofile.core.utils import echo_plain_green
from iprofile.core.utils import echo_plain_red
from iprofile.core.utils import echo_red
from iprofile.settings.registry import settings
from iprofile.utils.mixins import OSMixin
import click


class ICommand(OSMixin):

    settings_check = True
    settings_error = texts.ERROR_IPROFILE_NOT_INITIALIZED

    def __init__(self, _autorun=True, *args, **kwargs):
        self.settings = settings

        if not self.check_settings():
            self.red(self.settings_error)
        else:
            if _autorun:
                self.run(**kwargs.copy())

        kwargs.clear()
        super(ICommand, self).__init__(*args, **kwargs)

    def check_settings(self):
        if self.settings_check:
            if not (self.settings or self.settings.exists()):
                return False
        return True

    def run(self, **options):
        raise NotImplementedError

    def red(self, text):
        return echo_red(text)

    def pred(self, text):
        return echo_plain_red(text)

    def green(self, text):
        return echo_green(text)

    def pgreen(self, text):
        return echo_plain_green(text)


class Command(click.Command):

    def run(self, options):
        return (
            self.callback(_autorun=False).run(**options)
            if self.callback else None
        )
