# -*- coding: utf-8 -*-

from commands import getstatusoutput
import os

PROJECT_PATH = '{}/.iprofiles'.format(os.getcwd())
PROJECT_NAME = os.path.basename(os.getcwd())
IPROFILE_PATH = os.path.dirname(os.path.dirname(__file__))


def get_profile_path(profile_name):
    return '{}/{}'.format(PROJECT_PATH, profile_name)


def get_ipython_path(profile_name):
    result = getstatusoutput(
        'ipython locate profile {}_{}'.format(PROJECT_NAME, profile_name))
    return (
        result[1], '{}/startup'.format(result[1])
        if result[0] == 0 and result[1] else None
    )


def create_ipython_profile(profile_name):
    result = getstatusoutput(
        'ipython profile create {}_{}'.format(PROJECT_NAME, profile_name))
    return result[1] if result[0] == 0 and result[1] else None
