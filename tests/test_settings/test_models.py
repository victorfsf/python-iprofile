# -*- coding: utf-8 -*-

from iprofile.settings.models import SectionDict
from tests.utils import set_up
from tests.utils import settings
from tests.utils import tear_down


def test_sectiondict___repr__():
    sdict = SectionDict({}, {}, map={'test': 'test'})
    assert sdict.__repr__() == "{'test': 'test'}"


def test_sectiondict_get_paths():
    _map = {'test': {'test1': {'test2': {'test3': {'test4': 'test5'}}}}}
    sdict = SectionDict({}, {}, map=_map)
    assert sdict.get('test.test1.test2.test3.test4') == 'test5'
    assert sdict.get('test.test1.test2.test3.test4.test5') is None


def test_sectiondict_update():
    yamlmap = {'test': 'test_yaml'}
    sdict = SectionDict(yamlmap, {}, map={'test': 'test'})
    assert sdict.update({'test': 'test1'}) == yamlmap


def test_sectiondict_pop():
    yamlmap = {'test': 'test_yaml'}
    sdict = SectionDict(yamlmap, {}, map={'test': 'test'})
    assert sdict.pop('test') == 'test'


def test_sectiondict_save():
    set_up()
    sdict = SectionDict(settings, {}, map={'test': 'test'})
    assert sdict.save() == settings
    tear_down()


def test_yamlordereddict_pop():
    set_up()
    path = settings.get('path')
    assert settings.pop('path') == path
    tear_down()


def test_yamlordereddict_open():
    set_up()
    settings.base_section = None
    settings.open()
    tear_down()
