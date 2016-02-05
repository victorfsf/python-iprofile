# -*- coding: utf-8 -*-

from iprofile.core.decorators import iregister
from iprofile.cli.init import Init
from iprofile.core.utils import create_ipython_profile
from iprofile.core.utils import get_ipython_path
from glob2 import glob
import click
import os
import shutil


@iregister
@click.command()
@click.argument('name')
@click.option('--no-symlink', is_flag=True)
class Create(Init.callback):

    def run(self, **options):
        profile = super(Create.callback, self).run(**options)
        if profile:
            return self.save(profile, **options)

    def save(self, profile, **options):
        name = options.get('name')

        create_ipython_profile(name)
        ipython_path, startup_path = get_ipython_path(name)
        abs_profile_path = os.path.abspath(profile)
        shutil.rmtree(startup_path, ignore_errors=True)

        if options.get('no_symlink', False):
            shutil.copytree(abs_profile_path, startup_path)
        else:
            os.makedirs(startup_path)
            files = glob('{}/**'.format(abs_profile_path))
            for file_path in files:
                os.symlink(file_path, '{}/{}'.format(
                    startup_path, os.path.basename(file_path)))
