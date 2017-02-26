{% set install_params_python = {} %}
{% for version_available in readme.python_versions %}
{% if version_available.version == python.version %}
{% set install_params_python = install_params_python.update(version_available) %}
{% endif %}
{% endfor %}

## Installing Python

~~~
brew install python3
~~~

Installing `python3` via Homebrew should automatically install `pip3`. Use that to install `virtualenv`.

~~~
pip3 install virtualenv
~~~

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `{{ readme.working_directory_mac }}`):

~~~
virtualenv -p python3 {{ install_params_python.virtual_environment_name }}
~~~

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory_mac }}/{{ install_params_python.virtual_environment_name }}/`).

Next activate that virtual environment and install our Python dependencies:

~~~
source {{ install_params_python.virtual_environment_name }}/bin/activate
pip3 install -r {{ install_params_python.requirements_name }}
~~~

