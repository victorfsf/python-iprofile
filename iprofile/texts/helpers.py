# -*- coding: utf-8 -*-

# README
IPROFILE_READ_ME = """
    IProfile CLI

    A CLI for handling IPython 4+ profiles startup scripts
"""

# COMMANDS
HELP_ACTIVATE = "Set the active profile."
HELP_ACTIVE = "Show the active profile."
HELP_CONFIG = "Create or change a settings variable for IProfile."
HELP_CREATE = "Create a new profile."
HELP_DEACTIVATE = "Deactivate the active profile."
HELP_DELETE = "Completely delete the profile and its files."
HELP_DJANGO = "Open a Django shell using IProfile."
HELP_INIT = "Initialize IProfile."
HELP_LIST = "Show a list of all profiles."
HELP_SHELL = "Open IPython with a given profile name (or the active profile)."
HELP_GITIGNORE = "Add a default .gitignore file inside your iprofiles path."
HELP_APPEND = "Append a IProfile project path to your settings."
HELP_POP = "Remove a IProfile project path from your settings."

# OPTIONS
HELP_INIT_PATH = "Set the iprofile folder path/name."
HELP_INIT_ACTIVE = "Set the active profile."
HELP_NAMES_ONLY = "Show only the profiles names."
HELP_NO_INPUT = "Take no input from the command."
HELP_SETTINGS = "Set the Django settings module."
HELP_CREATE_ACTIVE = "Activate the new profile."
HELP_APPEND_FORCE = "Forcefully append a project path."
HELP_NO_IGNORE = (
    "Don't create the profile if there's already one "
    "with the same name in any project."
)
HELP_PROJECT_OPT = (
    "Set where IProfile will search for the given profile name."
)
