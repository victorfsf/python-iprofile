# -*- coding: utf-8 -*-

from iprofile.core.decorators import iregister
from iprofile.core.mixins import Command
from iprofile.core.utils import PROJECT_PATH
from iprofile.core.utils import IPROFILE_PATH
from iprofile.core.utils import get_profile_path
import click
import os
import shutil


@iregister
@click.command()
@click.argument('name')
class Init(Command):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(PROJECT_PATH):
            os.makedirs(PROJECT_PATH)

        if os.path.isdir(profile):
            click.echo(
                click.style(
                    "Profile '{}' already exists in this project!".format(
                        name), fg="red", bold=True
                )
            )
            return

        os.makedirs(profile)
        profile_items = ['00.ipy', '01.py']
        for item in profile_items:
            open('{}/{}'.format(profile, item), 'a').close()
        startup_readme = '{}/ipython/README'.format(IPROFILE_PATH)
        shutil.copy(startup_readme, profile)
        click.echo(
            "Profile path: '{}'".format(profile)
        )
        click.echo(
            click.style(
                "Created new Profile '{}'!".format(name),
                fg="green", bold=True
            )
        )
        return profile
