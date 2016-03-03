# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.profiles.models.mixins import IProfileCreate
from iprofile.profiles.models.mixins import IProfileDir
from iprofile.settings.registry import settings
from iprofile.utils.mixins import OSMixin
from iprofile.core.utils import echo_plain_green
from IPython.core.profiledir import ProfileDirError
from slugify import slugify
import IPython


class Profile(OSMixin):
    settings = None

    def __init__(self, name):
        settings.read()
        self.name = slugify(name)
        self.find_project(name)

    def find_project(self, name):
        self.dirname = self.absjoin(
            settings.get('path'), name
        )
        if self.isdir(self.dirname):
            return
        append = settings.get('append')
        if isinstance(append, dict):
            for project, path in append.items():
                if not path:
                    return
                abspath = self.absuser(path)
                if self.isdir(abspath):
                    dirname = self.join(abspath, name)
                    if self.isdir(dirname):
                        self.dirname = dirname
                        echo_plain_green(
                            texts.LOG_PROFILE_PROJECT_FOUND.format(project))
                        break

    def create(self):
        profile = IProfileCreate()
        profile.path = self.dirname
        profile.initialize()

    def locate(self):
        try:
            if not hasattr(self, '_iprofiledir'):
                self._iprofiledir = IProfileDir.find_profile_dir(self.dirname)
            return self._iprofiledir
        except ProfileDirError:
            return

    def exists(self):
        return True if self.locate() else False

    def activate(self):
        if self.exists():
            settings.update({
                'active': self.name
            }).save()

    def deactivate(self):
        settings.update({
            'active': None
        }).save()

    def delete(self):
        self.remove(self.dirname)

        active = settings.get('active')
        if self.name == active:
            self.deactivate()

        if hasattr(self, '_iprofiledir'):
            delattr(self, '_iprofiledir')

    def shell(self, options):
        IPython.start_ipython(
            argv=options + ['--profile-dir', self.dirname]
        )
