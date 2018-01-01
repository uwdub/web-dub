{% if docker is defined and docker.required %}
{% set install_params_docker_toolbox = {} %}
{% for version_available in readme.docker_toolbox_versions %}
{% if version_available.version == docker.toolbox.version %}
{% set install_params_docker_toolbox = install_params_docker_toolbox.update(version_available) %}
{% endif %}
{% endfor %}
## Installing Docker Toolbox

[{{ install_params_docker_toolbox.windows.installer_url }}]({{ install_params_docker_toolbox.windows.installer_url }})

This installer must be run by right-clicking and selecting 'Run as administrator'.
This is required even when using an Administrator account.
Otherwise, VirtualBox can fail to create the host-only network required for VirtualBox and Docker Toolbox.

When installing Docker Toolbox:

- On 'Select Destination Location':

  Set an installation path of {{ install_params_docker_toolbox.windows.install_path }}.

- On 'Select Components':

  Uncheck 'Kitematic for Windows'.

{% endif %}
