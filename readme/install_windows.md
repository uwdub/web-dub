# Dependency Installation for Windows

## Installing Python

[https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)

This documentation assumes an installation path of `c:/Python35`.

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip' and 'for all users (requires elevation)'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

- On 'Advanced Options':

  Set an installation path of `c:/Python35`.

  Uncheck all options.

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `c:/devel/web-jekyll-base`):

~~~
c:/Python35/python.exe -m venv env35
~~~

This will create a directory for the virtual environment (e.g., `c:/devel/web-jekyll-base/env35/`).

Next activate that virtual environment and install our Python dependencies:

~~~
env35/Scripts/activate.bat
pip install -r requirements3.txt
~~~

## Installing Node

[https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi](https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi)

The default installation options are appropriate.

## Installing Ruby

[https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.3.exe](https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.3.exe)

This documentation assumes an installation path of `c:/Ruby233`.

When installing Ruby:

- On 'Installation Destination and Optional Tasks':

  Set an installation path of `c:/Ruby233`.

  Check 'Add Ruby executables to your PATH'.

### Installing Ruby DevKit:

[https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe](https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

This documentation assumes an installation path of `c:/RubyDevKit`.

When installing the Ruby DevKit:

- Extract to `c:/RubyDevKit`.

- Install the DevKit into the Ruby installation:

  ~~~
  cd c:/RubyDevKit
  ruby dk.rb init
  ruby dk.rb install
  ~~~

