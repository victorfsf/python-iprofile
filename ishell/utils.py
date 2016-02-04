# -*- coding: utf-8 -*-

from commands import getstatusoutput
from ishell.config import registry


def get_profile_path(base_dir, profile_name=None):
    ishell_path = (
        '{}/.ishell'.format(base_dir) if base_dir else '.ishell'
    )
    if not profile_name:
        return ishell_path
    return ishell_path, '{}/{}'.format(ishell_path, profile_name)


def get_ipython_path(profile_name):
    return getstatusoutput(
        'ipython locate profile {}'.format(profile_name))[1]


def run_command(command, path='', *args):
    registry.get_command(command)(argv=args, path=path)
