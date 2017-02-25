{% set install_params_python = {} -%}
{%- for version_available in readme.python_versions -%}
  {%- if version_available.version == python.version -%}
    {%- set install_params_python = install_params_python.update(version_available) -%}
  {%- endif -%}
{%- endfor -%}

If it is not already active, you need to re-activate the virtual environment.
From the working directory of our project (e.g., `{{ readme.working_directory }}`):

    {{ install_params_python.virtual_environment_name }}/bin/activate
