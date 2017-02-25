{% set install_params_python = {} -%}
{%- for version_available in readme.python_versions -%}
  {%- if version_available.version == python.version -%}
    {%- set install_params_python = install_params_python.update(version_available) -%}
  {%- endif -%}
{%- endfor -%}

If it is not already active, you need to re-activate the virtual environment.
Move to the working directory of our project. (e.g., `cd {{ readme.working_directory_mac }}`)

Next activate that virtual environment:
`source {{ install_params_python.virtual_environment_name }}/bin/activate`