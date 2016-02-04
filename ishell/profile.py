# -*- coding: utf-8 -*-

from ishell.config import registry
from ishell.utils import get_ipython_path
from ishell.utils import get_profile_path
from commands import getstatusoutput
from glob2 import glob
import os
import shutil

ISHELL_DIR = os.path.dirname(os.path.dirname(__file__))


class CommandMeta(type):

    def __init__(cls, *args, **kwargs):
        if cls.name:
            registry.add(cls)


class BaseCommand(object):
    __metaclass__ = CommandMeta
    name = None

    def __init__(self, *args, **kwargs):
        self.path = kwargs.pop('path')
        self.run(args=kwargs.pop('argv', None))
        super(BaseCommand, self).__init__(*args, **kwargs)

    def run(self, args):
        raise NotImplementedError


class Create(BaseCommand):
    name = 'create'

    def run(self, args):
        ishell_path, profile_path = get_profile_path(self.path, args[0])

        if not os.path.isdir(ishell_path):
            os.makedirs(ishell_path)

        if os.path.isdir(profile_path):
            raise OSError('Profile already exists!')
        os.makedirs(profile_path)

        profile_items = ['00.ipy', '01.py']
        for item in profile_items:
            open('{}/{}'.format(profile_path, item), 'a').close()

        startup_readme = '{}/ishell/ipython/README'.format(ISHELL_DIR)
        shutil.copy(startup_readme, profile_path)


class Save(BaseCommand):
    name = 'save'

    def run(self, args):
        profile_name = args[0]
        ishell_path, profile_path = get_profile_path(self.path, profile_name)

        if not (os.path.isdir(ishell_path) and os.path.isdir(profile_path)):
            Create(argv=args, path=self.path)

        os.system('ipython profile create {}'.format(profile_name))
        ipython_path = getstatusoutput(
            'ipython locate profile {}'.format(profile_name))[1]
        startup_path = '{}/startup'.format(ipython_path)
        abs_profile_path = os.path.abspath(profile_path)
        shutil.rmtree(startup_path, ignore_errors=True)
        os.makedirs(startup_path)
        files = glob('{}/**'.format(abs_profile_path))
        for file_path in files:
            os.symlink(file_path, '{}/{}'.format(
                startup_path, os.path.basename(file_path)))


class Delete(BaseCommand):
    name = 'delete'

    def run(self, args):
        profile_name = args[0]
        _, profile_path = get_profile_path(self.path, args[0])
        ipython_path = get_ipython_path(profile_name)
        shutil.rmtree(profile_path, ignore_errors=True)
        shutil.rmtree(ipython_path, ignore_errors=True)


class RunIPython(BaseCommand):
    name = 'shell'

    def run(self, args):
        profile_name = args[0]
        from IPython import start_ipython
        start_ipython(argv=['--profile', profile_name])
