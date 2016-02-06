# -*- coding: utf-8 -*-


class Command(object):

    def __init__(self, _auto_run=True, *args, **kwargs):
        self.kwargs = kwargs.copy()
        if _auto_run:
            self.run(**self.kwargs)
        kwargs = {}
        super(Command, self).__init__(*args, **kwargs)

    def run(self, **options):
        raise NotImplementedError
