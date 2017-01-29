This is a template for websites implemented using Jekyll.

# Building the Site

This site is implemented in Jekyll, which requires Ruby and Node.js. It also uses Python for automation and testing.

## Installing Ruby, Ruby DevKit, Node.js, and Python

Development currently requires:

- Ruby 2.3.1

  [https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.1.exe](https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.3.1.exe)

  Installation on Windows:

  During installation:

  - On 'Installation Destination and Optional Tasks':

    Documentation assumes an installation path of c:\Ruby231.

    Check 'Add Ruby executables to your PATH'.

- Ruby DevKit

  [https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe](https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

  When installing the Ruby DevKit:

  - Extract to `c:\RubyDevKit`.

  - Install the DevKit into our Ruby installation:

    ~~~
    cd c:\RubyDevKit
    ruby dk.rb init
    ruby dk.rb install
    ~~~

- Node 4.5.0

  [https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi](https://nodejs.org/dist/v4.5.0/node-v4.5.0-x64.msi)

  When installing Node.js, the default options are appropriate.

- Python 3.5.2

  [https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)

  When installing Python:

  - Choose 'Customize Installation'
  - On 'Optional Features':

    Check 'pip' and 'for all users (requires elevation)'.

    Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

  - On 'Advanced Options':

    Uncheck all options.

    Set the installation path to `c:\Python35`.

## Creating a Virtual Environment and Installing Dependencies

All Python work should be done within a virtual environment, to avoid dependency conflicts.
Node.js and Ruby have their own dependency management (i.e., npm shrinkwrap and bundler).
Our Python automation scripts will employ those tools, but we first need to configure Python.

Create the virtual environment. From the working directory of our project (e.g., `c:\devel\web-jekyll-base`):

    c:\Python35\python.exe -m venv env35

This will create a directory for the virtual environment (e.g., `c:\devel\web-jekyll-base\env35\`).

Next activate that virtual environment and install our Python dependencies:

    env35\Scripts\activate.bat
    pip install -r requirements3.txt

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies

## Building and Serving the Site

Invoke automation is provided for building the site.

If it is not already active, you need to re-activate the virtual environment.
From the working directory of our project (e.g., `c:\devel\web-jekyll-base`):

    env35\Scripts\activate.bat

To build the site:

    invoke build_test

To build and serve the site on `localhost:4000`, continuously updating based on changes:

    invoke serve_test