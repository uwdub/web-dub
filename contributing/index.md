---
layout: base/sidebar-right
title: Website Contribution
---

<div class="sidebar_start"></div>
- Table of Contents
{:toc}
<div class="sidebar_end"></div>

Creating, maintaining, and enhancing the DUB website is ongoing community effort.
Many types of contribution are possible, from complaining, to simple content improvement, to major structural enhancements.
If you are interested in contributing, please start by reviewing this page's guidance.
If this page does not answer your questions on how to get started, let us know.

# Communication and Coordination <a name="communication-and-coordination"></a>

Our web development efforts are coordinated on several channels.

## Email

Anybody may contact dub-web via email:  

`insert a recaptcha mailhide here or something like that`

Anybody in the DUB community may also join dub-web:

<https://dub.washington.edu/mailman/listinfo/dub-web>

## GitHub

Development is hosted on GitHub at:
 
<https://github.com/uwdub/web-dub>

Our primary coordination mechanisms are Issues on this repository:

<https://github.com/uwdub/web-dub/issues>

## Slack

`insert something about a slack channel here`

# Types of Contributions

## Complaining

An always popular form of contribution is to complain about what has been done, 
complain about what has not been done, or suggest what could be done.
Please feel free to use any of the 
[Communication and Coordination](#communication-and-coordination) mechanisms.

A guiding principle of web-dub is that we will keep the website appropriately maintainable.
This means the website will also generally be minimal.
Please do not be offended when we consider your suggestion to be an unmaintainable monster that can never be allowed.

## Modifying a Single File

The most common form of contribution is updating some text.
If this is all you need, you can probably do this directly on GitHub.

GitHub explains how to edit a file via GitHub:

<https://help.github.com/articles/editing-files-in-another-user-s-repository/>

In short, you will need to:

- Have a GitHub account.
- Find the appropriate file in the repository:

  <https://github.com/uwdub/web-dub>
- Click the pencil icon for 'Edit this page'.
- Ignore the [Things to be Ignored](#things-to-be-ignored).
- Make your changes.
- Submit them as a pull request.

The pull request will be reviewed by web-dub and published when we accept it.
If you are doing something small and easy, that should be pretty quickly after you submit.

## Modifying Multiple Files

## Things to be Ignored <a name="things-to-be-ignored"></a>

The DUB website is implemented in 
[Jekyll](http://jekyllrb.com/), which in turn uses 
[Markdown](http://liquidmarkup.org/) and 
[Liquid](https://daringfireball.net/projects/markdown/syntax).
Layout and styling use [Bootstrap](http://getbootstrap.com/).

You should be able to mostly ignore this. 
If you are editing text, or changing a field in a header, things should 'just work'.
You should be find to find something in the site, modify or copy text, and get what you expect.

But if you are unsure about something, then you might need to understand something.

[Understanding Markdown](#understanding-markdown) can help if confused by the syntax of text, such as:

    # This is an HTML h1
    ### This is an HTML h3
    [This Is Link Text](http://this-is-a-link.com)
    <http://this-is-a-link-with-itself-as-the-text.com>

[Understanding the Jekyll Header](#understanding-the-jekyll-header) can help if confused by a page header, such as:

{% highlight yaml %}
---
layout: main-no-sidebar
current_page_item: "people"
---
{% endhighlight %}

[Understanding Liquid](#understanding-liquid) can help if confused by text containing
`{% raw %}{{{% endraw %}`, `{% raw %}}}{% endraw %}`, `{% raw %}{%{% endraw %}`, `{% raw %}%}{% endraw %}`, such as: 

{% highlight liquid %}
{% raw %}{%{% endraw %} for item_name in item_person.name offset: 1 {% raw %}%}{% endraw %}
  {% raw %}{{{% endraw %} item_name {% raw %}}}{% endraw %}
{% raw %}{%{% endraw %} endfor {% raw %}%}{% endraw %}
{% raw %}{{{% endraw %} item_person.name[0] {% raw %}}}{% endraw %}
{% endhighlight %}

[Understanding Jekyll](#understanding-jekyll) can help if confused by how site content is organized, 
or if considering a major structural enhancement.
If you are considering something major here, you really should first reach out to dub-web
via any of the [Communication and Coordination](#communication-and-coordination) mechanisms.

[Understanding Tests](#working-with-tests) can help if confused by how data consistency is enforced.
This is generally not visible in website content, as the tests are external.
But tests might be rejecting some edits you are submitting,
or you will need to understand tests if considering a major structural enhancement.
 
## Understanding Markdown <a name="understanding-markdown"></a>

## Understanding the Jekyll Header <a name="understanding-the-jekyll-header"></a>

## Understanding Liquid <a name="understanding-liquid"></a>

## Understanding Jekyll <a name="understanding-jekyll"></a>

## Understanding Tests <a name="understanding-tests"></a>

# Technology Guidance

## Installing Jekyll

We use Jekyll to build our websites. It requires Python 2.7 and Ruby.

First, [install Python 2.7]({{ site.baseurl }}/contributing.html#Python27_win).

Second, [install Ruby]({{ site.baseurl }}/contributing.html#Ruby_win).

Now we can install Jekyll:

    gem install jekyll

By convention, we use Fabric to ease deployment. It should be installed as part of `requirements2.txt`.

The `build` task will compile the site to `_site`.

    fab build

The `serve` task will continuously compile and serve the website on `localhost:4000`.

    fab serve

The `deploy` task will deploy the site to its production location.

    fab deploy

{% comment %}
We use Jekyll to build our websites. It requires Python 2.7 and Ruby.

The easiest way to install Jekyll on Mac is to first install [RubyGems](http://rubygems.org/pages/download). Once you do this, setting up Jekyll becomes simple.

    gem install jekyll

If you run into problems with this, you might need to install OSX Command Line Tools. Directions for doing so are available [here](http://railsapps.github.io/xcode-command-line-tools.html).

It's that easy (note how much shorter the directions are than the Windows ones!). By default, the above command will install all other dependencies.

By convention, we use Fabric to ease deployment. It should be installed as part of `requirements2.txt`.

The `build` task will compile the site to `_site`.

    fab build

The `serve` task will continuously compile and serve the website on `localhost:4000`.

    fab serve

The `deploy` task will deploy the site to its production location.

    fab deploy
{% endcomment %}

## Installing Ruby

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

## Installing Python 3

We should use Python 3 whenever possible. Currently that means Python 3.4.

First, [install Microsoft Visual Studio]({{ site.baseurl }}/contributing.html#MicrosoftVisualStudio). Be sure to note the need to configure environment variables to point Python 3.4 at the install.

You then need Python:

<https://www.python.org/ftp/python/3.4.1/python-3.4.1.msi>

Python 3.4 includes pip and pyvenv, so we just get started. By convention, we call our environment `env34`:

    c:\Python34\python.exe -m venv env34    

Now you can install your project requirements. By convention, we put these in `requirements3.txt`:

    env34\Scripts\activate.bat
    pip install -r requirements3.txt

If a module fails with an error `Unable to find vcvarsall.bat`, it is because Microsoft Visual Studio is not set up correctly.

## Installing Git and GitHub Clients

We use Git and GitHub.

First, download [git for Windows](http://git-scm.com/download/win).

Consider downloading [GitHub for Windows](https://windows.github.com/), which provides a graphical interface for interacting with git and GitHub.

By convention, GitHub for Windows defines the `upstream` remote:

    git remote add upstream <GitHub HTTPS clone URL>

For example, for [cse441-sp15](https://github.com/uwcse441/web-cse441-sp15) we define `upstream` as:

    git remote add upstream https://github.com/uwcse441/web-cse441-sp15.git

This ends up being a very useful convention, regardless of whether you're on Windows, Mac, Linux, or something we've never heard of.

{% comment %}
We use Git and GitHub.

First, download [git for Mac](http://git-scm.com/download/mac).

Consider downloading [GitHub for Mac](https://mac.github.com/), which provides a graphical interface for interacting with git and GitHub.

By convention, GitHub for Windows defines the `upstream` remote:

    git remote add upstream <GitHub HTTPS clone URL>

For example, for [cse441-sp15](https://github.com/uwcse441/web-cse441-sp15) we define `upstream` as:

    git remote add upstream https://github.com/uwcse441/web-cse441-sp15.git

This ends up being a very useful convention, regardless of whether you're on Windows, Mac, Linux, or something we've never heard of.
{% endcomment %}

## Git and Feature Branching








{% comment %}
## <a name="forking"></a> Forking the Repository

The easiest way to fork a repository is to visit the repository on GitHub and press the fork button. So for our course repository, visit [here](https://github.com/uwcse441/web-cse441-sp15).

![fork]({{ site.baseurl }}/images/development_general/fork.png)

And then you have a local version!

![forked]({{ site.baseurl }}/images/development_general/forked.png)

You can then clone it on your desktop and start editing.

![cloned]({{ site.baseurl }}/images/development_general/cloned.png)

You can also clone it via the desktop application. For example, on Mac:

![cloning_desktop]({{ site.baseurl }}/images/development_general/cloning_desktop.png)
    
## <a name="branches"></a>Branching Behavior

All of the directions in this section assume that you're using a command line. If you decided to use Git for Windows or Git for Mac, you'll need to navigate the user interface to do the same activities, but it should be fairly straightforward.

Git operates with an idea called _branches_. These are incredibly useful for keeping your code separate whenever possible. When you're working, create a separate branch for your code. For example, if I were making a branch to edit assignment 3, I might do the following:

	git checkout -b assignment3

Which checks out a new branch named `assignment3`. If you ever want to switch branches, you can check out a new branch. Such as: `git checkout master`.

You might also be able to achieve this via the desktop application. For example, on Mac:

![branching_desktop]({{ site.baseurl }}/images/development_general/branching_desktop.png)

Congrats! You now have your branch. You can now make whatever changes you need to _within that directory_.

To commit code, you first need to `add` your files with `git add`. For example, if I edited the `index.html` file, I would type:

	git add index.html
	
I can then `git commit` my work and add a message. However, this only commits the files _locally_; meaning they will only appear on my computer, but not to the rest of the internet! To resolve this, we `push` our code after committing:

	git push

This is usually pretty apparent via the desktop applications. Files usually are automatically checked to be added by default in the desktop applications.

## <a name="pull_request"></a> Submitting a Pull Request

After pushing a set of changes, a pull request appears in the parent repository (the [course website repository](https://github.com/uwcse441/web-cse441-sp15) in our case). It'll look something like the following:

![pull_request]({{ site.baseurl }}/images/development_general/pull_request.png)

Push the `pull request` button and send one off to us! We'll take a look, and accept your changes if they don't crash the website.
{% endcomment %}

{% comment %}
### <a name="MicrosoftVisualStudio"></a> Microsoft Visual Studio

Many Node.js and Python modules require a C compiler for included native code.

We currently use the freely available Microsoft Visual Studio C++ 2012 for Windows Desktop:

<http://go.microsoft.com/?linkid=9816758>

#### Versions

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

![VS90COMNTOOLS]({{ site.baseurl }}/images/development_general/vs90comntools.png)
![VS100COMNTOOLS]({{ site.baseurl }}/images/development_general/vs100comntools.png)
{% endcomment %}
