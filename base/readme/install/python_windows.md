{% set install_params_python = {} %}
{% for version_available in readme.python_versions %}
{% if version_available.version == python.version %}
{% set install_params_python = install_params_python.update(version_available) %}
{% endif %}
{% endfor %}
## Installing Python

[{{ install_params_python.windows.installer_url }}]({{ install_params_python.windows.installer_url }})

This documentation assumes an installation path of `{{ install_params_python.windows.install_path }}`.

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher', and 'for all users (requires elevation)'.

- On 'Advanced Options':

  Check 'Install for all users' and 'Precompile standard library'.

  Uncheck 'Create shortcuts for installed applications', 'Add Python to environment variables', 'Download debugging symbols', and 'Download debug binaries (requires VS 2015 or later)'.

  Set an installation path of `{{ install_params_python.windows.install_path }}`.

  Uncheck all options.

- On 'Setup was successful':

  If present, choose 'Disable path length limit'.

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `{{ readme.working_directory_windows }}`):

~~~
{{ install_params_python.windows.install_path }}/python.exe -m venv {{ install_params_python.virtual_environment_name }}
~~~

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory_windows }}/{{ install_params_python.virtual_environment_name }}/`).

Next activate that virtual environment and install our Python dependencies:

~~~
{{ install_params_python.virtual_environment_name }}/Scripts/activate.bat
pip install -r {{ install_params_python.requirements_name }}
~~~


