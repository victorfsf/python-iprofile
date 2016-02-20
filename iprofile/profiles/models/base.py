# -*- coding: utf-8 -*-

from iprofile.utils.mixins import OSMixin
from iprofile.settings.registry import settings
from iprofile.profiles.models.mixins import IProfileDir
from iprofile.profiles.models.mixins import IProfileCreate
from IPython.core.profiledir import ProfileDirError
from slugify import slugify


class Profile(OSMixin):
    settings = None

    def __init__(self, name, *args, **kwargs):
        settings.read()
        if not settings.exists():
            raise Exception
        self.name = slugify(name)
        self.dirname = self.absjoin(
            settings.get('profiles').get('path'), name
        )

    def create(self):
        profile = IProfileCreate()
        profile.initialize(self.dirname)

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
            settings.get('profiles').update({
                'active': self.name
            }).save()

    def deactivate(self):
        settings.get('profiles').update({
            'active': None
        }).save()

    def delete(self):
        self.remove(self.dirname)

        active = settings.get('profiles').get('active')
        if self.name == active:
            self.deactivate()

        if hasattr(self, '_iprofiledir'):
            delattr(self, '_iprofiledir')
