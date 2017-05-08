This is the beginning of a project template.

# Project Dependencies

Dependencies required for this project are:
- Python 3.5.2

# Windows Installation

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

Create the virtual environment. From the working directory of our project (e.g., `c:/devel/invoke-base`):

~~~
c:/Python35/python.exe -m venv env35
~~~

This will create a directory for the virtual environment (e.g., `c:/devel/invoke-base/env35/`).

Next activate that virtual environment and install our Python dependencies:

~~~
env35/Scripts/activate.bat
pip install -r requirements3.txt
~~~

# Mac Installation

## Installing Homebrew

This documentation assumes use of Homebrew: [https://brew.sh/](https://brew.sh/).

~~~
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~~~

The default installation options are appropriate.

## Installing Python

~~~
brew install python3
~~~

Installing `python3` via Homebrew should automatically install `pip3`. Use that to install `virtualenv`.

~~~
pip3 install virtualenv
~~~

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `~/Desktop/invoke-base`):

~~~
virtualenv -p python3 env35
~~~

This will create a directory for the virtual environment (e.g., `~/Desktop/invoke-base/env35/`).

Next activate that virtual environment and install our Python dependencies:

~~~
source env35/bin/activate
pip3 install -r requirements3.txt
~~~

