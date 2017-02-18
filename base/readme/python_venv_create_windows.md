{% set install_params_python = {} -%}
{%- for version_available in readme.python_versions -%}
  {%- if version_available.version == python.version -%}
    {%- set install_params_python = install_params_python.update(version_available) -%}
  {%- endif -%}
{%- endfor -%}

Create the virtual environment. From the working directory of our project (e.g., `{{ readme.working_directory }}`):

    {{ install_params_python.install_path }}\python.exe -m venv {{ install_params_python.virtual_environment_name }}

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory }}\{{ install_params_python.virtual_environment_name }}\`).

Next activate that virtual environment and install our Python dependencies:

    {{ install_params_python.virtual_environment_name }}\Scripts\activate.bat
    pip install -r {{ install_params_python.requirements_name }}

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies
