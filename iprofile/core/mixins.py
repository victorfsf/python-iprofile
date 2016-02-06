# -*- coding: utf-8 -*-

import click


class ICommand(object):

    def __init__(self, _autorun=True, *args, **kwargs):
        self.kwargs = kwargs.copy()
        if _autorun:
            self.run(**self.kwargs)
        kwargs = {}
        super(ICommand, self).__init__(*args, **kwargs)

    def run(self, **options):
        raise NotImplementedError


class Command(click.Command):

    def run(self, options):
        return (
            self.callback(_autorun=False).run(**options)
            if self.callback else None
        )
