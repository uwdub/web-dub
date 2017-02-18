{% set install_params_node = {} -%}
{%- for version_available in readme.node_versions -%}
{%- if version_available.version == node.version -%}
  {%- set install_params_node = install_params_node.update(version_available) -%}
{%- endif -%}
{%- endfor -%}

Latest version available: [{{ install_params_node.installer_url }}]({{ install_params_node.installer_url }})

When installing Node.js, the default options are appropriate.
