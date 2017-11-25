{% if docker is defined and docker.required %}
{% set install_params_docker_toolbox = {} %}
{% for version_available in readme.docker_toolbox_versions %}
{% if version_available.version == docker.toolbox.version %}
{% set install_params_docker_toolbox = install_params_docker_toolbox.update(version_available) %}
{% endif %}
{% endfor %}
## Installing Docker Toolbox

`TODO`
{% endif %}
