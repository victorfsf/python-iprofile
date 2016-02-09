# -*- coding: utf-8 -*-

from iprofile.core.utils import echo_red
from iprofile.core.utils import echo_green
from iprofile.core.utils import PROJECT_PATH
from slugify import slugify
import click


class ICommand(object):
    project_path = PROJECT_PATH

    def __init__(self, _autorun=True, *args, **kwargs):
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

    def slugify_name(self, options, pop=False):
        name = options.get('name', None) if not pop else options.pop('name')
        if not name:
            return None
        return slugify(name)


class Command(click.Command):

    def run(self, options):
        return (
            self.callback(_autorun=False).run(**options)
            if self.callback else None
        )
