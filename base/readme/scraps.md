
All Python work should be done within a virtual environment, to avoid dependency conflicts.
Node.js and Ruby have their own dependency management (i.e., npm shrinkwrap and bundler).
Our Python automation scripts will employ those tools, but we first need to configure Python.




Next use Python's invoke automation to get the rest of our dependencies:

    invoke update_dependencies
