# -*- coding: utf-8 -*-


class Command(object):

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs.copy()
        self.run(**self.kwargs)
        kwargs = {}
        super(Command, self).__init__(*args, **kwargs)

    def run(self, **options):
        raise NotImplementedError
