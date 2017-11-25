# Tasks

This project uses Invoke for task execution. Available tasks can be listed:

`invoke -l`

Available tasks include:

### build_production

Build the site to `_site`, using the production configuration in `_config-production.yml`.

`invoke build_production`

### build_test

Build the site to `_site`, using the test configuration in `_config-test.yml`.

`invoke build_test`

### compile_config

Compile files specified in `_base_config.yml`, via key `compile_config : entries`.

`invoke compile_config`

### compile_requirements

Compile `requirements3.txt` from `requirements3.txt.in`.

`invoke compile_requirements`

### docker_console

If the project uses Docker, open a console in the Docker virtual machine.

`invoke docker_console`

### docker_ip

If the project uses Docker, output the IP address of the Docker virtual machine.

`invoke docker_ip`

### docker_localize

If the project uses Docker, compile files specified in `_base_config.yml`, via key `compile_docker_localize : entries`.

`invoke docker_localize`

### docker_machine_ensure

If the project uses Docker, ensure the Docker virtual machine is created.

`invoke docker_machine_ensure`

### docker_start

If the project uses Docker, start the Docker containers specified in `tests/full/docker/test_compose.yml`.

`invoke docker_start`

### docker_stop

If the project uses Docker, stop the Docker containers specified in `tests/full/docker/test_compose.yml`.

`invoke docker_stop`

### serve_production

Serve the site on port 4000, using the production configuration in `_config-production.yml`.

`invoke serve_production`

### serve_test

Serve the site on port 4000, using the test configuration in `_config-test.yml`.

`invoke serve_test`

### update_base

Pull updates to this template.

`invoke update_base`

### update_dependencies

Ensure dependencies are installed.

`invoke update_depenencies`

