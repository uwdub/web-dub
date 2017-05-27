{% if docker is defined and docker.required %}
- Docker Toolbox {{ docker.toolbox.version }}

  Note we are using this version due to a potential bug in 1.12.5, which is unable to mount volumes on Windows.

  [https://github.com/docker/toolbox/issues/607](https://github.com/docker/toolbox/issues/607)
{% endif %}
