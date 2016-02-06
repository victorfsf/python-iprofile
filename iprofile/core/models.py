# -*- coding: utf-8 -*-

from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile.core.utils import PROJECT_PATH
import click


class ICommand(object):
    project_path = PROJECT_PATH

    def __init__(self, _autorun=True, *args, **kwargs):
        self.kwargs = kwargs.copy()
        if _autorun:
            self.run(**self.kwargs)
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
