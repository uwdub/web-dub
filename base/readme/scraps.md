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
