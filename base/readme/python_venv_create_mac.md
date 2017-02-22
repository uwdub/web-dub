{% set install_params_python = {} -%}
{%- for version_available in readme.python_versions -%}
  {%- if version_available.version == python.version -%}
    {%- set install_params_python = install_params_python.update(version_available) -%}
  {%- endif -%}
{%- endfor -%}

Installing `python3` via Homebrew should install `pip3` automatically.

Create the virtual environment using pip.
`pip3 install virtualenv`

Move to the working directory of our project. (e.g., `cd {{ readme.working_directory_mac }}`)

`virtualenv -p python3 {{ install_params_python.virtual_environment_name }}`

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory_mac }}/{{ install_params_python.virtual_environment_name }}/`).

Next activate that virtual environment and install our Python dependencies:

`source {{ install_params_python.virtual_environment_name }} activate`

Next activate that virtual environment and install our Python dependencies:

    {{ install_params_python.virtual_environment_name }}/bin/activate
    pip3 install -r {{ install_params_python.requirements_name }}

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies
