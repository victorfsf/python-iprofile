# -*- coding: utf-8 -*-

from slugify import slugify
import click
import os
import subprocess


PROJECT_PATH = '{0}/iprofiles'.format(os.getcwd())
PROJECT_NAME = os.path.basename(os.getcwd())


def get_ipython_name(profile_name):
    return '{0}_{1}'.format(slugify(PROJECT_NAME), profile_name)


def get_profile_path(profile_name):
    return '{0}/{1}'.format(PROJECT_PATH, profile_name)


def ipython_locate(profile_name):
    args = 'ipython locate profile {0}'.format(
        get_ipython_name(profile_name)).split()
    try:
        result = subprocess.check_output(
            args, stderr=subprocess.STDOUT,
            universal_newlines=True).replace('\n', '')
        return result
    except subprocess.CalledProcessError:
        return


def get_ipython_path(profile_name, profile_dir=None):

    if not profile_dir:
        profile_dir = get_profile_directory(profile_name)

    if profile_dir:
        profile_dir = get_user_home(profile_dir)
        return (
            profile_dir, '{0}/startup'.format(profile_dir),
            '{0}/ipython_config.py'.format(profile_dir)
        )

    ipython_path = ipython_locate(profile_name)
    return (
        ipython_path, '{0}/startup'.format(ipython_path),
        '{0}/ipython_config.py'.format(ipython_path)
    ) if ipython_path else (None, None, None)


def create_ipython_profile(profile_name, directory=None):
    args = 'ipython profile create {0}'.format(
        get_ipython_name(profile_name)).split()
    if directory:
        if not os.path.isdir(directory):
            os.makedirs(directory)
        args += ['--profile-dir', '"{0}"'.format(directory)]
    return subprocess.check_output(
        args, stderr=get_null_output(),
        universal_newlines=True).replace('\n', '')


def get_active_profile(config=None):
    if not config:
        config = read_config('{0}/.config'.format(PROJECT_PATH))
    return config.get('ACTIVE', None)


def get_django_settings_module(config=None):
    if not config:
        config = read_config('{0}/.config'.format(PROJECT_PATH))
    return config.get('DJANGO_SETTINGS_MODULE', None)


def echo_red(message):
    return click.echo(click.style(message, fg='red', bold=True))


def echo_green(message):
    return click.echo(click.style(message, fg='green', bold=True))


def get_null_output():
    try:
        return subprocess.DEVNULL
    except AttributeError:
        return open(os.devnull, 'wb')


def read_config(config_file):
    data = {}
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            data_list = f.readlines()
            for line in data_list:
                config, value = line.split('=', 1)
                data[config] = value.strip()
    return data


def save_config(config_file, data_list):
    with open(config_file, 'w') as f:
        for field, value in data_list.items():
            f.write('{0}={1}'.format(field, value))


def get_profile_directory(profile_name):
    profile_path = get_profile_path(profile_name)
    config_file = '{0}/.config'.format(profile_path)
    return get_user_home(read_config(config_file).get('PROFILE_DIR', None))


def get_user_home(directory):
    if directory and directory.startswith('~'):
        directory = directory.replace('~', os.path.expanduser('~'), 1)
    return directory


def list_profiles(project_path):
    return [
        x for x in os.listdir(project_path)
        if os.path.isdir('{0}/{1}'.format(project_path, x)) and
        'ipython_config.py' in os.listdir('{0}/{1}'.format(project_path, x))
    ]
