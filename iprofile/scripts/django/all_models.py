# -*- coding: utf-8 -*-


def load(__builtin__):
    from django.apps import apps

    for _, models in apps.all_models.items():
        for model in models.values():
            setattr(__builtin__, model.__name__, model)
