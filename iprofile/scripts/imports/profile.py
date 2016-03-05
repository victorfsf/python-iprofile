# -*- coding: utf-8 -*-


def load(__builtin__, profile_path, folder=None):
    import os
    profile_path = os.path.abspath(os.path.expanduser(profile_path))
    log_header = '[IProfile] Importing profile:'
    files = None

    if os.path.isdir(profile_path):
        from glob2 import glob
        startup = os.path.join(profile_path, 'startup')
        if os.path.isdir(startup):
            if folder:
                path = '{}/{}/**/*.py'.format(startup, folder)
            else:
                path = '{}/**/*.py'.format(startup)
            files = glob(path)
    elif os.path.isfile(profile_path):
        files = [profile_path]
    if files:
        import imp
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
            '{} Nothing was imported from "{}{}"'.format(
                log_header, profile_path,
                '/{}'.format(folder) if folder else '')
        )
