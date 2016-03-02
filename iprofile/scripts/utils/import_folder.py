# -*- coding: utf-8 -*-


def load(__builtin__, folder):
    from iprofile.settings.registry import settings
    import os

    files = None
    settings.read(ignore_errors=True)
    log_header = '[IProfile Script] import_folder:'
    folder = os.path.join(
        settings.get('path'),
        settings.get('lastshell'),
        'startup',
        folder
    )
    if os.path.isdir(folder):
        from glob2 import glob
        import imp

        files = glob('{}/**/*.py'.format(folder))
        for startup_file in files:
            module = imp.load_source('imported_module', startup_file)
            valid_items = (
                (x, y) for x, y in module.__dict__.items()
                if y and not x.startswith('__')
            )
            for name, mod in valid_items:
                setattr(__builtin__, name, mod)
    else:
        print(
            '{} Nothing was imported from "{}"'.format(log_header, folder)
        )
