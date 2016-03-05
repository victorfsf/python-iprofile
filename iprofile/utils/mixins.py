# -*- coding: utf-8 -*-

import os
import shutil


class OSMixin(object):

    def join(self, *args):
        return os.path.join(*args)

    def absjoin(self, *args):
        return os.path.abspath(self.join(*args))

    def absuser(self, *args):
        return os.path.abspath(os.path.expanduser(*args))

    def makedirs(self, path):
        try:
            os.makedirs(path)
        except OSError:
            pass

    def isfile(self, filename):
        return os.path.isfile(filename)

    def isdir(self, path):
        return os.path.isdir(path)

    def remove(self, path_or_file):
        if os.path.islink(path_or_file):
            os.unlink(path_or_file)
        elif os.path.isfile(path_or_file):
            os.remove(path_or_file)
        elif os.path.isdir(path_or_file):
            shutil.rmtree(path_or_file, ignore_errors=True)

    def new_file(self, filename, overwrite=False):
        if not self.isfile(filename) or overwrite:
            open(filename, 'w').close()

    def dirname(self, path_or_file):
        return os.path.dirname(path_or_file)
