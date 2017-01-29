This is the beginning of a project template.

## Installing Python

Development currently requires:

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