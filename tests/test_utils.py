# -*- coding: utf-8 -*-

from iprofile.utils.mixins import OSMixin
import os

mixin = OSMixin()


def test_osmixin_isdir():
    assert os.path.isdir('tests') == mixin.isdir('tests')


def test_osmixin_remove():
    open('test.txt', 'w').close()
    os.symlink('test.txt', 'testlink.txt')
    mixin.remove('testlink.txt')
    mixin.remove('test.txt')
    assert not mixin.isfile('test.txt')
    assert not mixin.isfile('testlink.txt')
