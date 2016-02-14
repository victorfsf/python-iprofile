# -*- coding: utf-8 -*-

from slugify import slugify
import click
import os


def get_ipython_name(profile_name, config):
    return '{0}_{1}'.format(
        slugify(
            config.get('project_name') or os.path.basename(os.getcwd())
        ),
        profile_name
    )


def echo_red(message):
    return click.echo(click.style(message, fg='red', bold=True))


def echo_green(message):
    return click.echo(click.style(message, fg='green', bold=True))


def get_user_home(directory):
    if directory and directory.startswith('~'):
        directory = directory.replace('~', os.path.expanduser('~'), 1)
    return directory


def list_profiles(project_path):
    if os.path.isdir(project_path):
        return [
            x for x in os.listdir(project_path)
            if os.path.isdir('{0}/{1}'.format(project_path, x)) and
            'settings.yml' in os.listdir('{0}/{1}'.format(project_path, x))
        ]
    return []


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass
