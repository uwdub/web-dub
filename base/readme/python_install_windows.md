{% set install_params_python = {} -%}
{%- for version_available in readme.python_versions -%}
  {%- if version_available.version == python.version -%}
    {%- set install_params_python = install_params_python.update(version_available) -%}
  {%- endif -%}
{%- endfor -%}

[{{ install_params_python.installer_url }}]({{ install_params_python.installer_url }})

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip' and 'for all users (requires elevation)'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

- On 'Advanced Options':

  Uncheck all options.

  Set the installation path to `{{ install_params_python.install_path }}`.
