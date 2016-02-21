# Sumary

- [Configuration Files](#configuration-files)
    - [File: iprofile.yml](#file-iprofile-yml)
    - [File: settings.yml](#file-settings-yml)

# Configuration Files

Below are the two types of configuration files. The `iprofile.yml` file is the global configuration, while each profile has its on `settings.yml` file.

## File: [iprofile.yml](#file-iprofile-yml)

You can set new variables values to this file by running:

```
$ iprofile config my_variable my_variable_value
```

Obviously, they'll only serve a purpose if IProfile needs then.

#### Default:

```yaml
# Sets the project name.
# This name will be used to create the IPython profile folder.
# Example: "profile_my_project_folder_my-profile"
project_name: my_project_folder

# Sets the path to create and find the project's profiles.
project_path: iprofiles/
```

#### Variables:

```yaml
# Sets the settings module for a Django application.
django_settings_module: my_project.settings

# Sets the active profile for the project.
active_profile: my-profile
```

## File: [settings.yml](#file-settings-yml)

You can set new variables values to this file by running:

```
$ iprofile config my_variable my_variable_value --profile my-profile
```

Obviously, they'll only serve a purpose if IProfile needs then.

#### Variables:

```yaml
# The IPython profile's path
ipython_path: /path/to/.ipython/profile_my_project_folder_my-profile
```
