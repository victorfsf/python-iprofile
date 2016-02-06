# -*- coding: utf-8 -*-

from iprofile.core.config import registry
import click


def iregister(command):
    def add_to_registry(command):
        registry.add(command)
        return command
    return add_to_registry(command)


def icommand(**kwargs):
    def command_wrapper(*cargs, **ckwargs):
        if not kwargs.get('options_metavar', None):
            kwargs.update({
                'options_metavar': '[<options>]'
            })
        func = cargs[0]
        command = click.decorators._make_command(
            func, kwargs.pop('name', func.__name__.lower()),
            kwargs, click.Command
        )
        command.__doc__ = func.__doc__
        iregister(command)
        return command
    return command_wrapper
