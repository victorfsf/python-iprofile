# -*- coding: utf-8 -*-

import click
import os


def echo_red(message):
    return click.echo(click.style(message, fg='red', bold=True))


def echo_plain_red(message):
    return click.echo(click.style(message, fg='red'))


def echo_green(message):
    return click.echo(click.style(message, fg='green', bold=True))


def echo_plain_green(message):
    return click.echo(click.style(message, fg='green'))


def get_user_home(directory):
    if directory and directory.startswith('~'):
        directory = directory.replace('~', os.path.expanduser('~'), 1)
    return os.path.abspath(directory)
