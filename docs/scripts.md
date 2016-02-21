# Sumary

- [Pre-made Scripts](#scripts)
    - [Python Scripts](#python-scripts)
        - [Importing all Django models](#importing-all-django-models)
    - [IPython Scripts](#ipython-scripts)
        - [Script: autoreload](#script-autoreload)

# Pre-made Scripts

IProfile comes with a module for pre-made scripts that can be imported in a startup script, then loaded. *Sadly, there's only two scripts right now.*

**NOTE:** IPython recognizes the magic attribute `__builtin__` in every Python version. It refers to the IPython shell itself (tested on IPython 4+).

## Python Scripts

### Importing all Django models

Open a startup script, like `iprofiles/startup/01_imports.py`, then paste the following code:

```python

from iprofile.scripts.django import all_models

all_models.load(__builtin__)

```

This script will import every model inside your Django project.

***

## IPython Scripts

IPython magic scripts can only be loaded by using the `magic` command:

```
$ iprofile PROFILE SCRIPT [FILENAME (without extension)]
```

### Script: [autoreload](#script-autoreload)

Adds the IPython's `%autoreload` module to a startup `*.ipy` file.

```
$ iprofile magic my_profile autoreload
```

***

### [^ Back to Top ^](#)
