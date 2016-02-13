# -*- coding: utf-8 -*-

from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile.models.config import GlobalConfig
import click


class ICommand(object):

    def __init__(self, _autorun=True, *args, **kwargs):
        self.global_config = GlobalConfig()
        self.global_config.read()
        self.project_path = self.global_config.get('project_path')

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
