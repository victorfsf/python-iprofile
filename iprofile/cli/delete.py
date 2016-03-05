# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_DELETE, short_help=texts.HELP_DELETE)
@click.argument('profile', required=False)
@click.option('--no-input', is_flag=True, help=texts.HELP_NO_INPUT)
@click.option('-p', '--project', required=False, help=texts.HELP_PROJECT_OPT)
class Delete(ICommand):

    def run(self, **options):
        name = options.get('profile')
        no_input = options.get('no_input')
        project = options.get('project')

        if not (name and slugify(name)):
            deleted = 0
            confirm_text = texts.INPUT_CONFIRM_DELETE_ALL
            if not (no_input or click.confirm(confirm_text)):
                return
            project_path = project or self.settings.get('path')
            for profile_name in self.list_profiles(project_path):
                if ':' in profile_name:
                    profile_name, project = profile_name.split(':')
                if self.delete(profile_name, project=project, delete_all=True):
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
            self.delete(name, project=project)

    def delete(self, name, project=None, delete_all=False):
        profile = Profile(name, project=project)

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
