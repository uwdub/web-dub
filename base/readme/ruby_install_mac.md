- Ruby:
  
  `brew install rbenv`
  
  Start rbenv whenever you open your terminal:
  
  `echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile`
  
  `source ~/.bash_profile`

  Install the correct version of Ruby:
  
  `rbenv install {{ ruby.version }}`
  
  `rbenv global {{ ruby.version }}`


  Alternatively, you can specify a Ruby version for the directory:
  
  `rbenv local {{ ruby.version }}`

- Ruby-Devkit:
  
  `ruby-devkit` is automatically installed when `rbenv` is installed.