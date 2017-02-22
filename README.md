This is the beginning of a project template.

## Homebrew Instructions for Mac

We recommend Homebrew for configuring your Mac system: [https://brew.sh/](https://brew.sh/).

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

The default options are appropriate.

# Installing Python

Development currently requires:

- Python 3.5.2

All Python work should be done within a virtual environment, to avoid dependency conflicts.
Node.js and Ruby have their own dependency management (i.e., npm shrinkwrap and bundler).
Our Python automation scripts will employ those tools, but we first need to configure Python.

## Windows Instructions

[https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)

When installing Python:

- Choose 'Customize Installation'
- On 'Optional Features':

  Check 'pip' and 'for all users (requires elevation)'.

  Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

- On 'Advanced Options':

  Uncheck all options.

  Set the installation path to `c:\Python35`.

### Creating a Virtual Environment and Installing Dependencies

Create the virtual environment. From the working directory of our project (e.g., `c:\devel\web-jekyll-base`):

    c:\Python35\python.exe -m venv env35

This will create a directory for the virtual environment (e.g., `c:\devel\web-jekyll-base\env35\`).

Next activate that virtual environment and install our Python dependencies:

    env35\Scripts\activate.bat
    pip install -r requirements3.txt

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies

## Mac Instructions

`brew install python3`

### Creating a Virtual Environment and Installing Dependencies

Installing `python3` via Homebrew should install `pip3` automatically.

Create the virtual environment using pip.
`pip3 install virtualenv`

Move to the working directory of our project. (e.g., `cd ~/Desktop/web-jekyll-base`)

`virtualenv -p python3 env35`

This will create a directory for the virtual environment (e.g., `~/Desktop/web-jekyll-base/env35/`).

Next activate that virtual environment and install our Python dependencies:

`source env35 activate`

Next activate that virtual environment and install our Python dependencies:

    env35/bin/activate
    pip3 install -r requirements3.txt

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies

# Installing Node

Development currently requires:

- Node 4.5.0


## Windows Instructions

Latest version available: [https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi](https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi)

When installing Node.js, the default options are appropriate.

## Mac Instructions

`brew install node`

# Installing Ruby

Development currently requires:

- Ruby 2.3.1
- Ruby DevKit

## Windows Instructions

  - Ruby:
  
  [https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.1.exe](https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.1.exe)

  During installation:

  - On 'Installation Destination and Optional Tasks':

    Documentation assumes an installation path of c:\Ruby231.

    Check 'Add Ruby executables to your PATH'.

- Ruby DevKit:

  [https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe](https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

  When installing the Ruby DevKit:

  - Extract to `c:\RubyDevKit`.

  - Install the DevKit into our Ruby installation:

    ~~~
    cd c:\RubyDevKit
    ruby dk.rb init
    ruby dk.rb install
    ~~~

## Mac Instructions

- Ruby:
  
  `brew install rbenv`
  
  Start rbenv whenever you open your terminal:
  
  `echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile`
  
  `source ~/.bash_profile`

  Install the correct version of Ruby:
  
  `rbenv install 2.3.1`
  
  `rbenv global 2.3.1`


  Alternatively, you can specify a Ruby version for the directory:
  
  `rbenv local 2.3.1`

- Ruby-Devkit:
  
  `ruby-devkit` is automatically installed when `rbenv` is installed.