# VimDE

VimDE is a simple Development Environment wrapper for vim and tmux.  It requires at least 
vim8 and python3.8. Here is a list of included plugins that come "out-of-the-box".  

* NERDTree  

* Deoplete-Jedi (for python autocompletion)

* Salt-vim syntax highligher

* Jinja2 syntax highligter

* Vimux (vim+tmux) integrated plugin

* Pudb python debugger (python3)

* Supertab vim plugin

* Over 900 vim colorschemes

* Powerline plugins for Vim and Tmux

* Wemux server for use with pair programming

## Local Development  

```
python -m venv .vimde-dev
source .vimde-dev/bin/activate
pip install --upgrade pip
pip install -q build
make dist install
make install
```
