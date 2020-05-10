%global deojedi_lc 42f4c24a951b0fb5e76a70e5234f16193a8a746d
%global deojedi_sc %(c=%{deojedi_lc}; echo ${c:0:7})

%global hug_lc 86e82de95e2a318589b718fef22eaeca1a3e3e04
%global hug_sc %(c=%{hug_lc}; echo ${c:0:7})

%global	jinja_lc b59d179defbc9fd6e6f426569f8430592e1a6a1b
%global jinja_sc %(c=%{jinja_lc}; echo ${c:0:7})

%global	muxtheme_lc 7c59902f64dcd7ea356e891274b21144d1ea5948
%global muxtheme_sc %(c=%{muxtheme_lc}; echo ${c:0:7})

%global	salt_lc	6ca9e3500cc39dd417b411435d58a1b720b331cc
%global salt_sc %(c=%{salt_lc}; echo ${c:0:7})

%global supertab_lc 40fe711e088e2ab346738233dd5adbb1be355172 
%global supertab_sc %(c=%{supertab_lc}; echo ${c:0:7})

%global vimcolor_lc 9e7ab1cfec5d3db85aa1c4e87329fd869ecf94e9
%global vimcolor_sc %(c=%{vimcolor_lc}; echo ${c:0:7})

%global	vimux_lc 37f41195e6369ac602a08ec61364906600b771f1
%global vimux_sc %(c=%{vimux_lc}; echo ${c:0:7})

%global	vundle_lc b255382d6242d7ea3877bf059d2934125e0c4d95
%global vundle_sc %(c=%{vundle_lc}; echo ${c:0:7})

%global yarp_lc b710bf4daccb603a423754794fb446e5fbb59576
%global yarp_sc %(c=%{yarp_lc}; echo ${c:0:7})


Name:           vimde
Version:        2020.4.0
Release:        1.eog%{?dist}
Summary:        Simple Development Environment based on Vim and tmux


License:        Apache 2.0
URL:            https://git.eogresources.com/eog/pkg-vimde

Source0:        https://git.eogresources.com/eog/pkg-vimde
Source1:	https://github.com/VundleVim/Vundle.vim/archive/%{vundle_lc}/Vundle.vim-%{vundle_sc}.tar.gz
Source2:	https://github.com/saltstack/salt-vim/archive/%{salt_lc}/salt_vim-%{salt_sc}.tar.gz
Source3:	https://github.com/Glench/Vim-Jinja2-Syntax/archive/%{jinja_lc}/Vim-Jinja2-Syntax-%{jinja_sc}.tar.gz
Source4:	https://github.com/benmills/vimux/archive/%{vimux_lc}/vimux-%{vimux_sc}.tar.gz
Source5:	https://github.com/jimeh/tmux-themepack/archive/%{muxtheme_lc}/tmux-themepack-%{muxtheme_sc}.tar.gz
Source6: 	https://github.com/flazz/vim-colorschemes/archive/%{vimcolor_lc}/vim-colorschemes-%{vimcolor_sc}.tar.gz
Source7:	https://github.com/vim-scripts/vim-auto-save/archive/0.1.7.tar.gz
Source8:	https://github.com/Shougo/deoplete.nvim/archive/5.2.tar.gz
Source9:	https://github.com/roxma/nvim-yarp/archive/%{yarp_lc}/nvim-yarp-%{yarp_sc}.tar.gz
Source10:	https://github.com/roxma/vim-hug-neovim-rpc/archive/%{hug_lc}/vim-hug-neovim-rpc-%{hug_sc}.tar.gz
Source11:	https://github.com/deoplete-plugins/deoplete-jedi/archive/%{deojedi_lc}/deoplete-jedi-%{deojedi_sc}.tar.gz
Source12:	https://github.com/ervandew/supertab/archive/%{supertab_lc}/supertab-%{supertab_sc}.tar.gz

Requires:	ctags
Requires:	git
Requires:	python3 >= 3.8
Requires:	python3-pudb
Requires:	python3-msgpack
Requires:	python3-neovim
Requires:	tmux >= 2.9
Requires:	tmux-powerline
Requires:	vim-enhanced >= 8.0
Requires: 	vim-fugitive
Requires:	vim-nerdtree
Requires:	vim-powerline
Requires: 	vim-syntastic-python
Requires: 	vim-syntastic-yaml
Requires: 	wemux


%description
A simple Vim based IDE using vim plugins for Saltstack and RPM based development.
VimDE can easily be extended by adding new plugins and editing your local .vimderc
file.  


%prep
%autosetup
# We simply need to untar the sources and copy them to /usr/share/vimde/bundle


%install


%files
%doc add-docs-here



%changelog
* Sat Apr 18 2020 Robby Callicotte <rcallicotte@gmail.com> - 2020.4.0-1.eog
- Initial build
