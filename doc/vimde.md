% vimde(1) 
% Robby Callicotte
% 2025.3

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
: Initialize the local user environment.  This creates local user directories 
  for plugins and generates default files. This command allows users to customize 
  `vimde` to their liking. 
  
`--update-plugins`, `-u`
: Updates plugins for `vimde`.  This is useful if you add additional plugins 
  to `~/.vimderc`.  

`--start`, `-s`
: Starts vimde.  This is the default option if none is given.

`--debug`, `-d`
: Starts vimde in debug mode.  This option prints runtime debug output to 
  `~/.vimde-debug.log`.

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

