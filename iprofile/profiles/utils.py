# -*- coding: utf-8 -*-

import IPython
import os


def get_ipython_dir():
    return IPython.paths.get_ipython_dir()


def list_profiles(project_path, project=None, show_project=True):
    if os.path.isdir(project_path):
        return [
            ('{}:{}'.format(x, project) if project and show_project else x)
            for x in os.listdir(project_path)
            if os.path.isdir(os.path.join(project_path, x)) and
            'ipython_config.py' in os.listdir(os.path.join(project_path, x))
        ]
    return []
