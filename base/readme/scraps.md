
All Python work should be done within a virtual environment, to avoid dependency conflicts.
Node.js and Ruby have their own dependency management (i.e., npm shrinkwrap and bundler).
Our Python automation scripts will employ those tools, but we first need to configure Python.




Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies




## Creating a Virtual Environment and Installing Dependencies

  {% set install_params_python = {} -%}
  {%- for version_available in readme.python_versions -%}
    {%- if version_available.version == local.python.version -%}
      {%- set install_params_python = install_params_python.update(version_available) -%}
    {%- endif -%}
  {%- endfor -%}

All Python work should be done within a virtual environment, to avoid dependency conflicts.

Create the virtual environment. From the working directory of our project (e.g., `{{ readme.working_directory }}`):

    {{ install_params_python.install_path }}\python.exe -m venv {{ install_params_python.virtual_environment_name }}

This will create a directory for the virtual environment (e.g., `{{ readme.working_directory }}\{{ install_params_python.virtual_environment_name }}\`).

Next activate that virtual environment and install our Python dependencies:

    {{ install_params_python.virtual_environment_name }}\Scripts\activate.bat
    pip install -r {{ install_params_python.requirements_name }}



## Starting Docker Containers and Running Tests

If it is not already active, you need to re-activate the virtual environment.
From the working directory of our project (e.g., `{{ readme.working_directory }}`):

    {{ install_params_python.virtual_environment_name }}\Scripts\activate.bat

To start Docker containers:

    invoke docker_start

To start a console in the Docker virtual machine:

    invoke docker_console

To run tests, assuming Docker containers have been started:

    nosetests
