# -*- coding: utf-8 -*-


def load(__builtin__, exclude_app=None):
    from django.apps import apps

    for app, models in apps.all_models.items():
        if not (exclude_app and app in exclude_app):
            for model in models.values():
                setattr(__builtin__, model.__name__, model)
