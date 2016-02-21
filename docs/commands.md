# Sumary

- [IProfile Command List](#iprofile-command-list)
- [Command: ACTIVATE](#command-activate)
- [Command: ACTIVE](#command-active)
- [Command: ADD](#command-add)
- [Command: CONFIG](#command-config)
- [Command: CREATE](#command-create)
- [Command: DEACTIVATE](#command-deactivate)
- [Command: DELETE](#command-delete)
- [Command: DJANGO](#command-django)
- [Command: INIT](#command-init)
- [Command: LIST](#command-list)
- [Command: MAGIC](#command-magic)
- [Command: SAVE](#command-save)
- [Command: SHELL](#command-shell)

***

## IProfile Command List

```
Usage: iprofile [OPTIONS] COMMAND [ARGS]...

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

***

## Command: [ACTIVATE](#command-activate)

###### Description: Set the active profile for IPython.

```
Usage: iprofile activate [OPTIONS] NAME

  Set the active profile for IPython.

Options:
  --help  Show this message and exit.
```

##### Example:

```
$ iprofile activate autoreload
```

***

## Command: [ACTIVE](#command-active)

###### Description: Show the active profile.

```
Usage: iprofile active [OPTIONS]

  Show the active profile.

Options:
  --help  Show this message and exit.
```

##### Example:

```
$ iprofile active
```

***

## Command: [ADD](#command-add)

###### Description: Create a new profile without saving it on IPython's path.

```
Usage: iprofile add [OPTIONS] NAME

  Create a new profile without saving it on IPython's path.

Options:
  --profile-dir PATH  Set the IPython profile path.
  --help              Show this message and exit.
```

##### Examples:

```
$ iprofile add autoreload
```

```
$ iprofile add autoreload --profile-dir="~/profiles/autoreload/"
```

***

## Command: [CLEAR](#command-clear)

###### Description: Remove the profile from IPython's path.

```
Usage: iprofile clear [OPTIONS] [NAME]

  Remove the profile from IPython's path.

Options:
  --no-input  Take no input from the command.
  --help      Show this message and exit.
```

##### Examples:

```
$ iprofile clear autoreload
```

```
$ iprofile clear --no-input
```

***

## Command: [CONFIG](#command-config)

###### Description: Create or change a configuration variable for IProfile.

```
Usage: iprofile config [OPTIONS] NAME VALUE

  Create or change a configuration variable for IProfile.

Options:
  --profile TEXT  Set a profile to apply the config.
  --help          Show this message and exit.
```

##### Examples:

```
$ iprofile config django myproject.settings
```

```
$ iprofile config project_path custom/path/my_profiles/
```

```
$ iprofile config ipython_path ~/profile_autoreload/ --profile autoreload
```

***

## Command: [CREATE](#command-create)

###### Description: Create a new profile and save it on IPython's path.

```
Usage: iprofile create [OPTIONS] NAME

  Create a new profile and save it on IPython's path.

Options:
  --no-symlink        Doesn't save the files as symlinks.
  --profile-dir PATH  Set the IPython profile path.
  --help              Show this message and exit.
```

##### Examples:

```
$ iprofile create autoreload
```

```
$ iprofile create autoreload --no-symlink
```

```
$ iprofile create autoreload --profile-dir="~/profiles/autoreload/"
```

```
$ iprofile create autoreload --no-symlink --profile-dir="~/profiles/autoreload/"
```

***

## Command: [DEACTIVATE](#command-deactivate)

###### Description: Deactivate the active profile for IPython.

```
Usage: iprofile deactivate [OPTIONS]

  Deactivate the active profile for IPython.

Options:
  --help  Show this message and exit.
```

##### Example:

```
$ iprofile deactivate
```

***

## Command: [DELETE](#command-delete)

###### Description: Completely delete the profile and its files.

```
Usage: iprofile delete [OPTIONS] [NAME]

  Completely delete the profile and its files.

Options:
  --no-input  Take no input from the command.
  --help      Show this message and exit.
```

##### Examples:

```
$ iprofile delete autoreload
```

```
$ iprofile delete --no-input
```

***

## Command: [DJANGO](#command-django)

###### Description: Open a Django shell using IProfile.

```
Usage: iprofile django [OPTIONS] [NAME] [IPYTHON_OPTIONS]...

  Open a Django shell using IProfile.

Options:
  --settings TEXT  Set an alternative Django settings module.
  --help           Show this message and exit.
```

##### Examples:

```
$ iprofile django . -- --no-autoindent --log-level=DEBUG
```

```
$ iprofile django autoreload -- --no-autoindent
```

```
$ iprofile django
```

```
$ iprofile django --settings custom.settings
```

```
$ iprofile django autoreload --settings custom.settings -- --log-level=DEBUG
```

***

## Command: [INIT](#command-init)

###### Description: Initialize IProfile.

```
Usage: iprofile init [OPTIONS] [PATH]

  Initialize IProfile.

Options:
  --help  Show this message and exit.

```

##### Examples:

```
$ iprofile init my_profiles
```

```
$ iprofile init
```

***

## Command: [LIST](#command-list)

###### Description: Show a list of all profiles.

```
Usage: iprofiles list [OPTIONS]

  Show a list of all profiles.

Options:
  --show-only [names|paths]  Show only the specified atribute.
  --help                     Show this message and exit.
```

##### Examples:

```
$ iprofile list
```

```
$ iprofile list --show-only names
```

```
$ iprofile list --show-only paths
```

***

## Command: [MAGIC](#command-magic)

###### Description: Load a IPython magic script.

```
Usage: iprofile magic [OPTIONS] PROFILE SCRIPT [FILENAME]

  Load a IPython magic script.

Options:
  --help  Show this message and exit.
```

##### Examples:

```
$ iprofile magic my_profile autoreload 00_autoreload
```

```
$ iprofile magic . autoreload 00_autoreload
```

```
$ iprofile magic my_profile autoreload
```

***
## Command: [SAVE](#command-save)

###### Description: Save changes to IPython's path.

```
Usage: iprofile save [OPTIONS] [NAME]

  Save changes to IPython's path.

Options:
  --no-symlink  Doesn't save the files as symlinks.
  --help        Show this message and exit.
```

##### Examples:

```
$ iprofile save autoreload
```

```
$ iprofile save autoreload --no-symlinks
```

***

## Command: [SHELL](#command-shell)

######  Open IPython with a given profile name (or the active profile).

```
Usage: iprofile shell [OPTIONS] [NAME] [IPYTHON_OPTIONS]...

  Open IPython with a given profile name (or the active profile).

Options:
  --help  Show this message and exit.
```

##### Examples:

```
$ iprofile shell
```

```
$ iprofile shell autoreload
```

```
$ iprofile shell autoreload -- --no-autoindent --log-level=DEBUG
```

```
$ iprofile shell . -- --no-autoindent --log-level=DEBUG
```

***

### [^ Back to Top ^](#)
