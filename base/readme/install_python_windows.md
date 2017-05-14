{% set install_params_python = {} %}
{% for version_available in readme.python_versions %}
{% if version_available.version == python.version %}
{% set install_params_python = install_params_python.update(version_available) %}
{% endif %}
{% endfor %}

## Installing Python

[{{ install_params_python.installer_url }}]({{ install_params_python.installer_url }})

This documentation assumes an installation path of `{{ install_params_python.install_path }}`.

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip' and 'for all users (requires elevation)'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

- On 'Advanced Options':

  Set an installation path of `{{ install_params_python.install_path }}`.

  Uncheck all options.

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `{{ readme.working_directory_windows }}`):

~~~
{{ install_params_python.install_path }}/python.exe -m venv {{ install_params_python.virtual_environment_name }}
~~~

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory_windows }}/{{ install_params_python.virtual_environment_name }}/`).

Next activate that virtual environment and install our Python dependencies:

~~~
{{ install_params_python.virtual_environment_name }}/Scripts/activate.bat
pip install -r {{ install_params_python.requirements_name }}
~~~

