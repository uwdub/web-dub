{% if ruby is defined and ruby.required %}

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
rbenv install {{ ruby.version }}
rbenv global {{ ruby.version }}
~~~

Alternatively, you can specify a Ruby version for the directory:

~~~
rbenv local {{ ruby.version }}
~~~

### Installing Ruby DevKit:

Installing `rbenv` via Homebrew should automatically install `ruby-devkit`
{% endif %}
