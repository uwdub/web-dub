{% if ruby is defined and ruby.required %}
{% set install_params_ruby = {} %}
{% for version_available in readme.ruby_versions %}
{% if version_available.version == ruby.version %}
{% set install_params_ruby = install_params_ruby.update(version_available) %}
{% endif %}
{% endfor %}
## Installing Ruby

[{{ install_params_ruby.windows.installer_url }}]({{ install_params_ruby.windows.installer_url }})

This documentation assumes an installation path of `{{ install_params_ruby.windows.install_path }}`.

When installing Ruby:

- On 'Installation Destination and Optional Tasks':

  Set an installation path of `{{ install_params_ruby.windows.install_path }}`.

  Check 'Add Ruby executables to your PATH'.

  Uncheck 'Associate .rb and .rbw files with this Ruby installation' and 'Use UTF-8 as default external encoding'.

- On 'Select Components':

  Check 'MSYS2 development toolchain 2018-06-24'.

- On 'Completing the Ruby 2.5.1-2-x86 with MSYS2 Setup Wizard':

  Check 'Run 'ridk install' to setup MSYS2 and development toolchain.

- On 'Ruby Installer 2 for Windows'

  Press Enter for '[1, 2, 3]'.

  Press Enter for '[]'.

{% endif %}
