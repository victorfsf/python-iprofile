# -*- coding: utf-8 -*-

from iprofile.core.config import registry
from iprofile.core.models import Command
import click


def iregister(command):
    def registry_wrapper(command):
        registry.add(command)
        return command
    return registry_wrapper(command)


def icommand(**kwargs):
    def command_wrapper(*cargs):
        func = cargs[0]
        command = click.command(
            kwargs.pop('name', func.__name__.lower()),
            kwargs.pop('cls', Command), **kwargs
        )(func)
        command.__doc__ = func.__doc__
        iregister(command)
        return command
    return command_wrapper
