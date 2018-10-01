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

Create the virtual environment. From the working directory of our project (e.g., `c:/devel/web-jekyll-base`):

~~~
c:\Python36/python.exe -m venv env36
~~~

This will create a directory for the virtual environment (e.g., `c:/devel/web-jekyll-base/env36/`).

Next activate that virtual environment and install our Python dependencies:

~~~
env36/Scripts/activate.bat
pip install -r requirements3.txt
~~~

## Installing Node

[https://nodejs.org/dist/v8.12.0/node-v8.12.0-x64.msi](https://nodejs.org/dist/v8.12.0/node-v8.12.0-x64.msi)

The default installation options are appropriate.

## Installing Ruby

[https://github.com/oneclick/rubyinstaller2/releases/download/rubyinstaller-2.5.1-2/rubyinstaller-devkit-2.5.1-2-x86.exe](https://github.com/oneclick/rubyinstaller2/releases/download/rubyinstaller-2.5.1-2/rubyinstaller-devkit-2.5.1-2-x86.exe)

This documentation assumes an installation path of `c:\Ruby251`.

When installing Ruby:

- On 'Installation Destination and Optional Tasks':

  Set an installation path of `c:\Ruby251`.

  Check 'Add Ruby executables to your PATH'.

  Uncheck 'Associate .rb and .rbw files with this Ruby installation' and 'Use UTF-8 as default external encoding'.

- On 'Select Components':

  Check 'MSYS2 development toolchain 2018-06-24'.

- On 'Completing the Ruby 2.5.1-2-x86 with MSYS2 Setup Wizard':

  Check 'Run 'ridk install' to setup MSYS2 and development toolchain.

- On 'Ruby Installer 2 for Windows'

  Press Enter for '[1, 2, 3]'.

  Press Enter for '[]'.

