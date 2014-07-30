---
layout: default
title: General Development Guide
---

This page documents some of our development tools and conventions. It aims to be thorough as possible while
remaining generic. Individual projects then document their own installation and configuration details.

## <a name="Git"></a> Git, GitHub, and GitHub for Windows

We use Git, GitHub, and GitHub for Windows.

By convention, we define the `upstream` remote:

    git remote add upstream <GitHub HTTPS clone URL>

For example, when developing for [web-jayfo](https://github.com/fogies/web-jayfo) define `upstream` as:

    git remote add upstream https://github.com/fogies/web-jayfo.git

## <a name="Jekyll"></a> Jekyll

We use Jekyll to build our websites. It requires Python 2.7 and Ruby.

First, [install Python 2.7]({{ site.baseurl }}/development_general.html#Python27).

Second, [install Ruby]({{ site.baseurl }}/development_general.html#Ruby).

Now we can install Jekyll:

    gem install jekyll

By convention, we use Jekyll to ease deployment.

First, [install Fabric]({{ site.baseurl }}/development_general.html#Fabric).

The `serve` task will then continuously and serve the website on `localhost:4000`.

    fab serve

The `deploy` task will deploy the site to its production location.

    fab deploy

## <a name="MicrosoftVisualStudio"></a> Microsoft Visual Studio

Many Node.js and Python modules require a C compiler for included native code.

We currently use the freely available Microsoft Visual Studio C++ 2012 for Windows Desktop:

<http://go.microsoft.com/?linkid=9816758>

### Versions

Node.js and Python each expect particular versions of Microsoft Visual Studio. Currently, that expectation is:

  * Node.js: Microsoft Visual Studio C++ 2012
  * Python 3.4: Microsoft Visual Studio C++ 2010
  * Python 2.7: Microsoft Visual Studio C++ 2008

Each version defines environment variables that say where to find the build tools:

  * `VS110COMNTOOLS` is defined by Microsoft Visual Studio C++ 2012
  * `VS100COMNTOOLS` is defined by Microsoft Visual Studio C++ 2010
  * `VS90COMNTOOLS` is defined by Microsoft Visual Studio C++ 2008

Instead of installing all of these versions, we manipulate the environment variables to alias the old versions to the newer version. This is not necessarily 100% robust, but has not been problematic.

This can be done locally within a session:

    set VS90COMNTOOLS="%VS110COMNTOOLS%"
    set VS100COMNTOOLS="%VS110COMNTOOLS%"

Alternatively, we can define the system environment variable:

     Control Panel
     System and Security
     System
     Advanced system settings
     Environment Variables...
     System variables
     New...

![VS90COMNTOOLS]({{ site.baseurl }}/img/development_general/vs90comntools.png)
![VS100COMNTOOLS]({{ site.baseurl }}/img/development_general/vs100comntools.png)

## <a name="Node.js"></a> Node.js

When I first tried to install Node.js, a tree fell on my house. Seriously. So first check you are not under any trees.

First, [install Microsoft Visual Studio]({{ site.baseurl }}/development_general.html#MicrosoftVisualStudio).

You then need Node.js:

<http://nodejs.org/download/>

Unfortunately, the current installers seem to require a reboot for path settings to take effect.

You should then be sure to understand the difference between global and local modules:

<http://blog.nodejs.org/2011/03/23/npm-1-0-global-vs-local-installation/>

Following the advice "install it in both places", we install several modules globally. These each have commands that it is convenient to be able to easily execute.

Cordova/PhoneGap enables mobile applications based on HTML, CSS, and Javascript:

    npm -g install cordova
    npm -g install phonegap

Ionic works with Cordova/PhoneGap and Angular to target mobile apps:

    npm -g install ionic

And you should install a project's local dependencies:

    npm install

## <a name="Python27"></a> Python 2.7

We use Python 2.7 as little as possible, but there are still libraries that require it.

First, [install Microsoft Visual Studio]({{ site.baseurl }}/development_general.html#MicrosoftVisualStudio). Be sure to note the need to configure environment variables to point Python 2.7 at the install.

You then need Python:

<https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi>

Python 2.7 does not come with a built-in package manager, so we need to install it. Download these two files:

<https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py>

<https://raw.github.com/pypa/pip/master/contrib/get-pip.py>

Then you can install pip:

    c:\Python27\python ez_setup.py
    c:\Python27\python get-pip.py

Now you need virtualenv:

    c:\Python27\Scripts\pip install virtualenv

Finally you can create a Python environment for your project. By convention, we call our environment `env27`:

    c:\Python27\Scripts\virtualenv.exe env27

Now you can install your project requirements. By convention, we put these in `requirements2.txt`:

    env27\Scripts\activate.bat
    pip install -r requirements2.txt

If a module fails with an error `Unable to find vcvarsall.bat`, it is because Microsoft Visual Studio is not set up correctly.

## <a name="Python34"></a> Python 3.4

We should use Python 3 whenever possible. Currently that means Python 3.4.

First, [install Microsoft Visual Studio]({{ site.baseurl }}/development_general.html#MicrosoftVisualStudio). Be sure to note the need to configure environment variables to point Python 3.4 at the install.

You then need Python:

<https://www.python.org/ftp/python/3.4.1/python-3.4.1.msi>

Python 3.4 includes pip and pyvenv, so we just get started. By convention, we call our environment `env34`:

    c:\Python34\Tools\Scripts\pyvenv.py env34

Now you can install your project requirements. By convention, we put these in `requirements3.txt`:

    env34\Scripts\activate.bat
    pip install -r requirements3.txt

If a module fails with an error `Unable to find vcvarsall.bat`, it is because Microsoft Visual Studio is not set up correctly.

## <a name="Ruby"></a> Ruby

To install Ruby, you need Ruby and an associated DevKit. You can get them here:

<http://rubyinstaller.org/downloads/>

Per the recommendations of the Ruby folks, I am using the 1.93 versions. First install Ruby:

<http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-1.9.3-p545.exe?direct>

During the install:

  * I use the install path `c:\Ruby193`
  * Ensure Checked "Add Ruby executables to your PATH"

Then install the Ruby DevKit:

<https://github.com/downloads/oneclick/rubyinstaller/DevKit-tdm-32-4.5.2-20111229-1559-sfx.exe>

Unzip it to a permanent directory. I use `c:\RubyDevKit`. Then install the DevKit:

    cd c:\RubyDevKit
    ruby dk.rb init
    ruby dk.rb install