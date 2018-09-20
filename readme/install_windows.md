# Dependency Installation for Windows

## Installing Python

[https://www.python.org/ftp/python/3.6.6/python-3.6.6.exe](https://www.python.org/ftp/python/3.6.6/python-3.6.6.exe)

This documentation assumes an installation path of `c:\Python36`.

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher', and 'for all users (requires elevation)'.

- On 'Advanced Options':

  Check 'Install for all users' and 'Precompile standard library'.

  Uncheck 'Create shortcuts for installed applications', 'Add Python to environment variables', 'Download debugging symbols', and 'Download debug binaries (requires VS 2015 or later)'.

  Set an installation path of `c:\Python36`.

  Uncheck all options.

- On 'Setup was successful':

  If present, choose 'Disable path length limit'.

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `c:\devel\invoke-base`):

~~~
c:\Python36/python.exe -m venv env36
~~~

This will create a directory for the virtual environment (e.g., `c:\devel\invoke-base/env36/`).

Next activate that virtual environment and install our Python dependencies:

~~~
env36/Scripts/activate.bat
pip install -r requirements3.txt
~~~

