# Sumary

- [Installation](#installation)
- [Why use it?](#why-use-it)
- [Usage](#usage)
    - [Running IProfile](#running-iprofile)
    - [Creating a new Profile](#creating-a-new-profile)
        - [Adding a Profile on your project](#adding-a-profile-on-your-project)
        - [Saving the Profile](#saving-the-profile)
        - [Creating the Profile](#creating-the-profile)
        - [Editing the startup files](#editing-the-startup-files)
    - [Opening IPython shell](#opening-ipython-shell)
        - [Activating a Profile](#activating-a-profile)
        - [Deactivating a Profile](#deactivating-a-profile)
        - [Checking which Profile is active](#checking-which-profile-is-active)
        - [Using IPython Options](#using-ipython-options)
        - [Using the Django shell](#using-the-django-shell)
    - [Deleting Profiles](#deleting-profiles)
        - [Removing only the IPython Profile](#removing-only-the-ipython-profile)
        - [Completely removing the profile](#completely-removing-the-profile)
    - [Listing Profiles](#listing-profiles)

## Installation

Install via pip:

```
$ pip install python-iprofile
```

## Why use it?

- IProfile will provide you with a portable way of creating and managing your IPython profiles startup scripts: instead of importing everything via `%cpaste` or line by line, all you need to do is create, edit it with your configurations and run your profile by using the provided CLI.

- The profiles you created will show up in your project's directory, as a part of it. Just edit or add files to your profiles and then run the [shell](#opening-the-ipython-shell).

# Usage

Bellow you'll find instructions on how to properly use the CLI. If you need a more organized way to learn about the commands, check the [Command Reference](https://github.com/victorfsf/python-iprofile/blob/master/docs/commands.md) page. Also, check out the [Scripts](https://github.com/victorfsf/python-iprofile/blob/master/docs/scripts.md) page for some pre-made scripts, the [Configuration](https://github.com/victorfsf/python-iprofile/blob/master/docs/configuration.md) page to understand how the configuration files work and the [Changelog](https://github.com/victorfsf/python-iprofile/wiki/Changelog) page for some changes and new features.

## Running IProfile

```
$ iprofile [--help]
```

###### Output:

```
Usage: -c [OPTIONS] COMMAND [ARGS]...

  IProfile CLI

  A CLI for handling IPython 4+ profiles startup scripts

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  activate    Set the active profile for IPython.
  active      Show the active profile.
  add         Create a new profile without saving it on IPython's path.
  clear       Remove the profile from IPython's path.
  config      Create or change a configuration variable for IProfile.
  create      Create a new profile and save it on IPython's path.
  deactivate  Deactivate the active profile for IPython.
  delete      Completely delete the profile and its files.
  django      Open a Django shell using IProfile.
  init        Initialize IProfile.
  list        Show a list of all profiles.
  magic       Load a IPython magic script.
  save        Save changes to IPython's path.
  shell       Open IPython with a given profile name (or the active profile).
```

## Creating a new Profile

There are three ways to create a profile:

- Initializing it on your project, locally (without sending it to IPython's folder).
- Creating it without symlinks (so every change on existing files needs to be [saved](#saving-the-profile).
- Creating it with symlinks (so every change on existing files will be saved automatically).

#### Adding a Profile on your project

Let's consider a project named `potatoes` and I want to create a new profile to activate the IPython's `%autoreload` config.

```
$ iprofile add autoreload
```

###### Output:

```
Created a new Profile 'autoreload'!
Profile path: '/path/to/potatoes/iprofiles/autoreload/'
```

#### Saving the Profile

```
$ iprofile save autoreload [--no-symlink]
```

###### Output:

```
Saving files as symlinks... **
IPython path: '/path/to/.ipython/profile_potatoes_autoreload/'
Profile saved!


[**] Saving files without symlinks... -> in case you set the --no-symlink option
```

#### Creating the Profile

By Creating it, you can skip the `add` and `save` commands above.

```
$ iprofile create autoreload [--no-symlink]
```

###### Output:

```
Created a new Profile 'autoreload'!
Profile path: '/path/to/potatoes/iprofiles/autoreload/'
Saving files as symlinks... **
IPython path: '/path/to/.ipython/profile_potatoes_autoreload/'
Profile saved!


[**] Saving files without symlinks... -> in case you set the --no-symlink option
```

#### Editing the startup files

Once you create your profile, you'll see a folder `iprofiles` in your project's root directory. Here's how it will look like for a profile called `autoreload`:

```
iprofiles
└── autoreload
    ├── ipython_config.py
    └── startup
        ├── 00_config.ipy
        ├── 01_imports.py
        └── README
```

The `*.py` and `*.ipy` files are empty by default, so you'll need to edit the ones you need. Let's put the `%autoreload` config inside the `00_config.ipy` file:

```
%load_ext autoreload
%autoreload 2
```

Remember to [save](#saving-the-profile) the profile if you used the `add` command or didn't create symlinks.

You can also add new files to the `startup` folder, but you'll need to run the `save` command everytime a file is created, edited or renamed **and you didn't create symlinks**. If the symlinks were created, everything that's inside the `startup` folder will automatically update after any change.

## Opening IPython shell

Once you have a profile, you can simply run the command bellow to open the IPython shell with your profile settings.

```
$ iprofile shell autoreload
```

#### Activating a Profile

Activating a profile will give you the power to open the shell without typing the profile's name.

```
$ iprofile activate autoreload
```

Once activated, all you got to do to open the shell with your profile settings is:

```
$ iprofile shell
```

#### Deactivating a Profile

If you want to deactivate the profile, just run:

```
$ iprofile deactivate
```

#### Checking which Profile is active

To see which profile is active, run:

```
$ iprofile active
```

#### Using IPython Options

The IPython shell comes with a load of optional parameters to use, which can be called through the shell command by running:

```
$ iprofile shell autoreload -- [IPython Options]
```

So, if you want to use the `--no-autoindent` and `--log-level=DEBUG` options:

```
$ iprofile shell autoreload -- --no-autoindent --log-level=DEBUG
```

**IMPORTANT**: If the profile name is not defined, put a dot before using the IPython options:

```
$ iprofile shell . -- --confirm-exit
```

#### Using the Django shell

*Only works with Django 1.7 or greater.*

You can also open a Django shell by setting the `DJANGO_SETTINGS_MODULE` config on `iprofile.yml`:

```
$ iprofile config django path.to.settings
```

After that, just run:

```
$ iprofile django autoreload
```

Or, for another settings:

```
$ iprofile django autoreload --settings path.to.another.settings
```

The Django shell command works exactly like the normal shell, so everything said on this [topic](#opening-ipython-shell) also applies to it.

## Deleting Profiles

You can delete your profile in two ways:


#### Removing only the IPython Profile

Keeps the profile on your project, but it will not be recognized by IPython. Specify the profile's name:

```
$ iprofile clear autoreload
```

If no name is specified, it will clear every Profile you have listed on your project (but it will prompt you first):

```
$ iprofile clear [--no-input]
```

###### Output:

```
Are you sure you want to delete all your profiles? [y/N]: y
Attempting to remove IPython profile at '/path/to/.ipython/profile_potatoes_autoreload/'...
IPython profile 'profile_potatoes_autoreload' successfully removed!
Successfully cleared 1 profile.
```

#### Completely removing the profile

Specify the profile's name:

```
$ iprofile delete autoreload
```

If no name is specified, it will delete every Profile you have listed on your project (but it will prompt you first):


```
$ iprofile delete [--no-input]
```

###### Output:

```
Are you sure you want to delete all your profiles? [y/N]: y
Attempting to remove IPython profile at '/path/to/.ipython/profile_potatoes_autoreload/'...
IPython profile 'profile_potatoes_autoreload' successfully removed!
Successfully cleared 1 profile.
Attempting to remove profile at '/path/to/potatoes/iprofiles/autoreload/'...
Profile 'autoreload' successfully removed!
Successfully deleted 1 profile.
```

## Listing Profiles

To list all the profiles inside your project, run:

```
$ iprofile list
```

###### Output:

```
1 profile was found:

Name: autoreload
IPython profile path:	/path/to/.ipython/profile_potatoes_autoreload
Project profile path:	/path/to/potatoes/iprofiles/autoreload
```

If you just want the profiles **names**, then run:

```
$ iprofile list --show-only names
```

###### Output:

```
autoreload
```

If you just want the profiles **paths**, then run:

```
$ iprofile list --show-only paths
```

###### Output:

```
/path/to/.ipython/profile_potatoes_autoreload
```

***

### [^ Back to Top ^](#)
