% vimde(1)
% vimde Authors
% 2020-

# NAME

vimde - Simple Development Environment based on Vim and Tmux

# SYNOPSIS

`vimde [options]`

# DESCRIPTION

`vimde` is an IDE tool for writing programs and running tests.  It is a wrapper 
around vim and tmux with a carefully curated list of default plugins.

## Command Line Options

The following command line parameters are understood.

`--init`, `-i`
: Initialize the environment.  This effectively creates local user directories 
  for plugins and generates default `vimrc` file, known as `vimderc` and 
  `tmuxderc` files.  This command must be ran first before starting `vimde`.

`--update-plugins`, `-u`
: Updates plugins for `vimde`.  This is useful if you add additional plugins 
  to `.vimderc`.  

