# Tasks

This project uses Invoke for task execution. Available tasks can be listed:

`invoke -l`

Available tasks include:

###### compile_config

Compile files specified in `_base_config.yml`, key `compile_config : entries`.

invoke `compile_config` 

###### compile_requirements

Compile `requirements3.txt` from `requirements3.txt.in`.

invoke `compile_requirements` 

###### docker_console

###### docker_ip

###### docker_localize

###### docker_machine_ensure

###### docker_start

###### docker_stop

