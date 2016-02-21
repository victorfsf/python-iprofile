# -*- coding: utf-8 -*-

from iprofile.utils.mixins import OSMixin
import os

mixin = OSMixin()


def test_osmixin_isdir():
    assert os.path.isdir('test') == mixin.isdir('test')


def test_osmixin_remove():
    open('test.txt', 'w').close()
    os.symlink('test.txt', 'testlink.txt')
    mixin.remove('testlink.txt')
    mixin.remove('test.txt')
