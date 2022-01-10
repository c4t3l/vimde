% vimde(1) 
% vimde Authors 
% 2022.01.00

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
  for plugins and generates default files. This command must be ran first 
  before starting `vimde`.  
  
`--update-plugins`, `-u`
: Updates plugins for `vimde`.  This is useful if you add additional plugins 
  to `.vimderc`.  

`--start`, `-s`
: Starts vimde.  This is the default option if none is given.

# ON-LINE HELP

Type ":help vimde" in `vimde` to get started. 

# FILES

`/usr/share/vimde/bundle/*` 
: Contains all of the default plugins and syntax highlighers for `vimde`.

`/usr/share/tmuxde/plugins/tmux-themepack*`
: Contains themepacks for tmux-powerline.  

`/etc/vimderc`
: System-wide `vimde-vim` initializations.

`/etc/tmuxderc`
: System-wide `vimde-tmux` initializations.

`~/.vimderc`
: Your personal `vimde-vim` customizations.

`~/.tmuxderc`
: Your personal `vimde-tmux` customizations.

