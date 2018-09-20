# Dependency Installation for Mac

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
virtualenv -p python3 env36
~~~

This will create a directory for the virtual environment (e.g., `~/Desktop/invoke-base/env36/`).

Next activate that virtual environment and install our Python dependencies:

~~~
source env36/bin/activate
pip3 install -r requirements3.txt
~~~

