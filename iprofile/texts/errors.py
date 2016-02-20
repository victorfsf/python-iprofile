# -*- coding: utf-8 -*-

ERROR_PROFILE_EXISTS = "Profile '{0}' already exists in this project!"
ERROR_PROFILE_DOESNT_EXIST_RUN = (
    "The profile '{0}' does not exist!\nRun 'iprofile create {0}'"
    " to create it."
)
ERROR_IPYTHON_PROFILE_DOESNT_EXIST = (
    "The IPython profile '{0}' does not exist!"
)
ERROR_PROFILE_DOESNT_EXIST = "The Profile '{0}' does not exist!"
ERROR_PROFILE_NOT_ACTIVE = (
    "The Profile '{0}' can't be deactivated: it's not even active!"
)
ERROR_NO_ACTIVE_PROFILE = "There are no active profiles on this project."
ERROR_NO_PROFILES_TO_SAVE = "There are no profiles to save."
ERROR_NO_PROFILES_TO_CLEAR = "There are no profiles to clear."
ERROR_NO_PROFILES_TO_LIST = "There are no profiles to list."
ERROR_NO_PROFILES_TO_DELETE = "There are no profiles to delete."
ERROR_DJANGO_WITHOUT_SETTINGS = (
    "Could not find variable 'django_settings_module'.\n"
    "Run 'iprofile config django [SETTINGS MODULE]' to set it."
)
ERROR_DJANGO_INVALID_SETTINGS = "Could not find settings module '{0}'."
ERROR_INIT_PATH_EXISTS = "The folder '{0}' already exists in this project!"
ERROR_IPYTHON_SCRIPT_DOESNT_EXIST = "Could not find script with name '{0}'."
ERROR_IPROFILE_NOT_INITIALIZED = (
    "IProfile was not initialized.\nRun 'iprofile init --help' for help."
)
ERROR_INIT_SETTINGS_EXIST = (
    "IProfile is already initialized."
)
