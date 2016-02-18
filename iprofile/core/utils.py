# -*- coding: utf-8 -*-

from iprofile.settings.utils import PROFILE_SETTINGS_FILE
import click
import os


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
            if os.path.isdir(os.path.join(project_path, x)) and
            PROFILE_SETTINGS_FILE in os.listdir(os.path.join(project_path, x))
        ]
    return []
