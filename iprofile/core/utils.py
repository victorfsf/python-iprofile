# -*- coding: utf-8 -*-

from slugify import slugify
import click
import os
import subprocess


PROJECT_PATH = '{}/.iprofiles'.format(os.getcwd())
PROJECT_NAME = os.path.basename(os.getcwd())


def get_ipython_name(profile_name):
    return '{}_{}'.format(slugify(PROJECT_NAME), profile_name)


def get_profile_path(profile_name):
    return '{}/{}'.format(PROJECT_PATH, profile_name)


def get_ipython_path(profile_name):
    args = 'ipython locate profile {}'.format(
        get_ipython_name(profile_name)).split(' ')
    try:
        result = subprocess.check_output(
            args, stderr=subprocess.STDOUT,
            universal_newlines=True).replace('\n', '')
        return result, '{}/startup'.format(result)
    except subprocess.CalledProcessError:
        return None, None


def create_ipython_profile(profile_name):
    args = 'ipython profile create {}'.format(
        get_ipython_name(profile_name)).split(' ')
    return subprocess.check_output(
        args, stderr=subprocess.STDOUT,
        universal_newlines=True).replace('\n', '')


def echo_red(message):
    return click.echo(click.style(message, fg='red', bold=True))


def echo_green(message):
    return click.echo(click.style(message, fg='green', bold=True))
