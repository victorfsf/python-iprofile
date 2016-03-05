# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from slugify import slugify
import click


@icommand(help=texts.HELP_APPEND, short_help=texts.HELP_APPEND)
@click.argument('name')
@click.argument('path')
@click.option('-f', '--force', is_flag=True, help=texts.HELP_APPEND_FORCE)
class Append(ICommand):

    def run(self, **options):
        slug, name = slugify(options.get('name')), options.get('name')
        path = self.absuser(options.get('path'))
        append = self.settings.get('append')

        if not slug:
            self.red(texts.ERROR_PROJECT_INVALID_NAME.format(name))
            return

        if not self.isdir(path):
            self.red(texts.ERROR_NO_SUCH_DIRECTORY.format(path))
            return

        if not options.get('force') and append.get(slug):
            self.red(texts.ERROR_APPEND_PROJECT_EXISTS.format(slug))
            return

        append.update({
            slug: str(path)
        })
        self.settings.update({
            'append': append
        }).save()
        self.green(texts.LOG_APPEND_PROJECT.format(slug, path))
