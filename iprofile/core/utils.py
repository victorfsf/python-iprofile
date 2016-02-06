# -*- coding: utf-8 -*-

from commands import getstatusoutput
from slugify import slugify
import click
import os

PROJECT_PATH = '{}/.iprofiles'.format(os.getcwd())
PROJECT_NAME = os.path.basename(os.getcwd())


def get_ipython_name(profile_name):
    return '{}_{}'.format(slugify(PROJECT_NAME), profile_name)


def get_profile_path(profile_name):
    return '{}/{}'.format(PROJECT_PATH, profile_name)


def get_ipython_path(profile_name):
    result = getstatusoutput(
        'ipython locate profile {}'.format(get_ipython_name(profile_name)))
    return (
        result[1], '{}/startup'.format(result[1])
        if result[0] == 0 and result[1] else None
    )


def create_ipython_profile(profile_name):
    result = getstatusoutput(
        'ipython profile create {}_{}'.format(PROJECT_NAME, profile_name))
    return result[1] if result[0] == 0 and result[1] else None


def echo_red(message):
    return click.echo(click.style(message, fg='red', bold=True))


def echo_green(message):
    return click.echo(click.style(message, fg='green', bold=True))
