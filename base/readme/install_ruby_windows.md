{% if ruby is defined and ruby.required %}
{% set install_params_ruby = {} %}
{% for version_available in readme.ruby_versions %}
{% if version_available.version == ruby.version %}
{% set install_params_ruby = install_params_ruby.update(version_available) %}
{% endif %}
{% endfor %}

## Installing Ruby

[{{ install_params_ruby.installer_url }}]({{ install_params_ruby.installer_url }})

This documentation assumes an installation path of `{{ install_params_ruby.install_path }}`.

When installing Ruby:

- On 'Installation Destination and Optional Tasks':

  Set an installation path of `{{ install_params_ruby.install_path }}`.

  Check 'Add Ruby executables to your PATH'.

### Installing Ruby DevKit:

[{{ install_params_ruby.installer_devkit_url }}]({{ install_params_ruby.installer_devkit_url }})

This documentation assumes an installation path of `{{ install_params_ruby.install_devkit_path }}`.

When installing the Ruby DevKit:

- Extract to `{{ install_params_ruby.install_devkit_path }}`.

- Install the DevKit into the Ruby installation:

  ~~~
  cd {{ install_params_ruby.install_devkit_path }}
  ruby dk.rb init
  ruby dk.rb install
  ~~~
{% endif %}
