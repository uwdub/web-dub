---
layout: base/bar-sidebar-none
title: Development Guide

working_directory: web-fogies
---

# Building a Jekyll Site

This site is implemented in Jekyll, thus requiring Ruby and Node.js. We also use Python in our automation and testing.

{% comment %}
Packages installed by the above can sometimes require a native compiler, for which we use Microsoft Visual Studio.
{% endcomment %}

## Installing Node.js, Python, Ruby, and Ruby DevKit

We currently use:

- [Node.js 5.1.0 - https://nodejs.org/dist/v5.1.0/node-v5.1.0-x64.msi](https://nodejs.org/dist/v5.1.0/node-v5.1.0-x64.msi)

  When installing Node.js, the default options are appropriate.

- [Python 3.5.0 - https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe](https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe)

  When installing Python:

  - Choose 'Customize Installation'
  - On 'Optional Features':

    Check 'pip' and 'for all users (requires elevation)'.

    Uncheck 'Documentation', 'tcl/tk and IDLE', 'Python test suite', 'py launcher'.

  - On 'Advanced Options':
 
    Uncheck all options.
  
    Set the installation path to `c:\Python35`.

- [Ruby 2.2.3 - https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.2.3.exe](https://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.2.3.exe)

  When installing Ruby:

  - On 'Installation Destination and Optional Tasks':
 
    Set the installation path to `c:\Ruby223`.
  
    Check 'Add Ruby executables to your PATH'.

- [Ruby DevKit - https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe](https://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

  When installing the Ruby DevKit:

  - Extract to `c:\RubyDevKit`.

  - Install the DevKit into our Ruby installation:
  
    ~~~
    cd c:\RubyDevKit
    ruby dk.rb init
    ruby dk.rb install
    ~~~

{% comment %}
## Installing Microsoft Visual Studio

Many Node.js and Python packages require a C compiler for included native code. We currently use:

[Microsoft Visual Studio C++ 2012 for Windows Desktop - https://go.microsoft.com/?linkid=9816758](https://go.microsoft.com/?linkid=9816758)

Node.js and Python each expect particular versions of Microsoft Visual Studio. Currently, that expectation is:

- Node.js: Microsoft Visual Studio C++ 2012
- Python 3.5: Microsoft Visual Studio C++ 2010

Each version defines environment variables that say where to find the build tools:

- `VS110COMNTOOLS` is defined by Microsoft Visual Studio C++ 2012
- `VS100COMNTOOLS` is defined by Microsoft Visual Studio C++ 2010

Instead of installing these versions, we manipulate environment variables to alias the old versions to the newer version. 
This is not necessarily completely robust, but has not been problematic.

This can be done locally within a command line session:

    set VS100COMNTOOLS="%VS110COMNTOOLS%"

But we generally define the system environment variable:

    Control Panel
    System and Security
    System
    Advanced system settings
    Environment Variables...
    System variables
    New...

![VS100COMNTOOLS]({{ site.baseurl }}/development/vs100comntools.png)
{% endcomment %}

## Creating a Virtual Environment and Installing Dependencies

All Python work should be done within a virtual environment, to avoid dependency conflicts.
Node.js and Ruby have their own dependency management (i.e., npm shrinkwrap and bundler).
Our Python automation scripts will employ those tools, but we first need to configure Python.

Create the virtual environment. From the working directory of our project (e.g., `c:\devel\{{ page.working_directory }}\`):

    c:\Python35\python.exe -m venv env35    

This will create a directory for the virtual environment (e.g., `c:\devel\{{ page.working_directory }}\env35\`).

Next activate that virtual environment and install our Python dependencies: 

    env35\Scripts\activate.bat
    pip install -r requirements3.txt

Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies

{% comment %}
If a package fails with an error `Unable to find vcvarsall.bat`, it is because Microsoft Visual Studio is not set up correctly.
{% endcomment %}

## Building and Serving the Site

Invoke automation is provided for building the site.  

If it is not already active, you need to re-activate the virtual environment.
From the working directory of our project (e.g., `c:\devel\{{ page.working_directory }}\`):

    env35\Scripts\activate.bat

To build the site:
    
    invoke build

To build and serve the site on `localhost:4000`, continuously updating based on changes:

    invoke serve
