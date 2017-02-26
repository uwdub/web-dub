{% if node is defined and node.required %}
{% set install_params_node = {} %}
{% for version_available in readme.node_versions %}
{% if version_available.version == node.version %}
{% set install_params_node = install_params_node.update(version_available) %}
{% endif %}
{% endfor %}

## Installing Node

[{{ install_params_node.installer_url }}]({{ install_params_node.installer_url }})

The default installation options are appropriate.
{% endif %}
