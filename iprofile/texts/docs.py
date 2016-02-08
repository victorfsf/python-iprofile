# -*- coding: utf-8 -*-
# flake8: noqa


IPYTHON_READ_ME = """This is the IPython startup directory

.py and .ipy files in this directory will be run *prior* to any code or files specified
via the exec_lines or exec_files configurables whenever you load this profile.

Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.::
    00-first.py
    50-middle.py
    99-last.ipy

To update/add new files (or if you set the '--no-symlink' option, or created this with the 'init' command), run:
    iprofile save {0} [--no-symlink]
"""


IPROFILE_READ_ME = """
    IProfile CLI

    A CLI for handling IPython 4+ profiles startup scripts
"""
