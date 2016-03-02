# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from iprofile.profiles.utils import list_profiles
from slugify import slugify
import click
import IPython


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('profile', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
class Shell(ICommand):

    def run(self, **options):
        ipython_options = list(options.get('ipython_options', []))

        name = options.get('profile')
        if not (name and slugify(name)):
            active = self.settings.get('active')
            profiles_list = list_profiles(self.settings.get('path'))
            if active and active in profiles_list:
                profile = Profile(active)
            else:
                profile = None
        else:
            profile = Profile(name)

        if not profile:
            IPython.start_ipython(argv=ipython_options)
            return

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(profile.name))
            return

        self.settings.update({
            'lastshell': profile.name
        }).save()

        profile.shell(ipython_options)
