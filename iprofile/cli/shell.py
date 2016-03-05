# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click
import IPython


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('profile', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('-p', '--project', required=False, help=texts.HELP_PROJECT_OPT)
class Shell(ICommand):

    def run(self, **options):
        ipython_options = list(options.get('ipython_options', []))
        project = options.get('project')
        name = options.get('profile')

        if not (name and slugify(name)):
            active = self.settings.get('active')
            profiles_list = self.list_profiles(
                self.settings.get('path'), show_project=True)

            if active and active in profiles_list:
                if ':' in active:
                    active_name, active_project = active.split(':')
                    profile = Profile(active_name, project=active_project)
                else:
                    profile = Profile(active, project=project)
            else:
                profile = None
        else:
            profile = Profile(name, project=project)

        if not profile:
            IPython.start_ipython(argv=ipython_options)
            return

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(profile.name))
            return

        self.settings.update({
            'last': profile.name
        }).save()

        profile.shell(ipython_options)
