## Tasks

This project uses Invoke for task execution. Available tasks can be listed:

`invoke -l`

See [Additional Task Documentation]({{ readme.url_github }}/{{ readme.url_github_readme_basedir }}/invoke.md).

Frequently used tasks will include:

{% for task in readme.invoke_readme_frequent %}
### {{ task }}

{% include readme.invoke_readme_paths[task] %} 

{% endfor %}

