# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.utils import list_profiles
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('profile', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
class Delete(ICommand):

    def run(self, **options):
        name = options.get('profile')
        no_input = options.get('no_input')

        if not (name and slugify(name)):
            project_path = self.settings.get('path')
            deleted = 0
            confirm_text = texts.INPUT_CONFIRM_DELETE_ALL
            if not (no_input or click.confirm(confirm_text)):
                return

            for profile_name in list_profiles(project_path):
                if self.delete(profile_name, delete_all=True):
                    deleted += 1
            if deleted > 0:
                click.echo()
                self.green(texts.LOG_QTT_DELETED.format(
                    deleted, 's' if deleted != 1 else ''))
            else:
                self.red(texts.ERROR_NO_PROFILES_TO_DELETE)
        else:
            confirm_text = texts.INPUT_CONFIRM_DELETE.format(name)
            if not (no_input or click.confirm(confirm_text)):
                return
            self.delete(name)

    def delete(self, name, delete_all=False):
        profile = Profile(name)

        if not profile.exists():
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST.format(name))
            return

        profile.delete()
        delete_text = texts.LOG_DELETE_PROFILE.format(name)
        if delete_all:
            self.pgreen(delete_text)
        else:
            self.green(delete_text)

        return True
