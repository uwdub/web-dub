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

Create the virtual environment. From the working directory of our project (e.g., `~/Desktop/web-jekyll-base`):

~~~
virtualenv -p python3 env35
~~~

This will create a directory for the virtual environment (e.g., `~/Desktop/web-jekyll-base/env35/`).

Next activate that virtual environment and install our Python dependencies:

~~~
source env35/bin/activate
pip3 install -r requirements3.txt
~~~

## Installing Node

~~~
brew install node
~~~

## Installing Ruby

~~~
brew install rbenv
~~~

Configure the terminal to include `rbenv`:

~~~
echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile`
source ~/.bash_profile`
~~~

Install the correct version of Ruby:

~~~
rbenv install 2.3.3
rbenv global 2.3.3
~~~

Alternatively, you can specify a Ruby version for the directory:

~~~
rbenv local 2.3.3
~~~

### Installing Ruby DevKit:

Installing `rbenv` via Homebrew should automatically install `ruby-devkit`

