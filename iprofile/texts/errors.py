# -*- coding: utf-8 -*-

ERROR_PROFILE_DOESNT_EXIST_RUN = (
    "The profile '{0}' does not exist!\nRun 'iprofile create {0}'"
    " to create it."
)
ERROR_IPYTHON_PROFILE_DOESNT_EXIST = (
    "The IPython profile '{}' does not exist!"
)
ERROR_NO_PROFILES_TO_DELETE = "There are no profiles to delete."
ERROR_NO_ACTIVE_PROFILE = "There are no active profiles on this project."
ERROR_NO_PROFILES_TO_LIST = "There are no profiles to list."
ERROR_DJANGO_WITHOUT_SETTINGS = (
    "Could not find settings variable 'django'.\n"
    "Run 'iprofile config django [SETTINGS MODULE]' to set it."
)
ERROR_DJANGO_INVALID_SETTINGS = "Could not find settings module '{}'."
ERROR_PROFILE_EXISTS = "Profile '{}' already exists in this project!"
ERROR_PROFILE_DOESNT_EXIST = "Profile '{}' does not exist!"
ERROR_IPROFILE_NOT_INITIALIZED = (
    "IProfile was not initialized.\nRun 'iprofile init --help' for help."
)
ERROR_INIT_SETTINGS_EXIST = (
    "IProfile is already initialized."
)
ERROR_PROFILE_INVALID_NAME = "Invalid name for profile: '{}'."
ERROR_INVALID_CONFIG = "Invalid settings variable: '{}'."
ERROR_INVALID_VALUE_CONFIG = "Invalid value for settings variable '{}': '{}'."
ERROR_GITIGNORE = "IProfile's .gitignore file already exists!"
