# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
import click


@icommand(help=texts.HELP_GITIGNORE, short_help=texts.HELP_GITIGNORE)
class GitIgnore(ICommand):

    content = (
        '**/security',
        '**/pid',
        '**/log',
        '**/db',
        '**/history.sqlite',
    )

    def run(self, **options):
        path = self.settings.get('path')
        gitignore = self.absjoin(path, '.gitignore')

        if self.isfile(gitignore):
            self.red(texts.ERROR_GITIGNORE)
            return

        self.makedirs(path)
        with open(gitignore, 'w') as f:
            f.write('\n'.join(self.content))

        self.green(texts.LOG_GITIGNORE)
        click.echo(gitignore)
