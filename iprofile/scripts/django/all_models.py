# -*- coding: utf-8 -*-


def load(__builtin__, exclude=[]):
    from django.apps import apps

    for app, models in apps.all_models.items():
        if app not in exclude:
            for model in models.values():
                setattr(__builtin__, model.__name__, model)
