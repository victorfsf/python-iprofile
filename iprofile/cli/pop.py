# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from slugify import slugify
import click


@icommand(help=texts.HELP_POP, short_help=texts.HELP_POP)
@click.argument('name')
class Pop(ICommand):

    def run(self, **options):
        slug, name = slugify(options.get('name')), options.get('name')
        append = self.settings.get('append')

        if not slug:
            self.red(texts.ERROR_PROJECT_INVALID_NAME.format(name))
            return

        if not append.get(slug):
            self.red(texts.ERROR_POP_PROJECT_DOESNT_EXIST.format(slug))
            return

        path = append.pop(slug)
        self.settings.save()
        self.green(texts.LOG_POP_PROJECT.format(slug, path))
