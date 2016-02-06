# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.models import ICommand
from iprofile.core.utils import get_profile_path
import os


class ActivateDeactivateMixin(ICommand):

    def run(self, **options):
        name = options.get('name')
        profile = get_profile_path(name)

        if not os.path.isdir(profile):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return
        return name
