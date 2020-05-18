%global deojedi_lc 42f4c24a951b0fb5e76a70e5234f16193a8a746d
%global deojedi_sc %(c=%{deojedi_lc}; echo ${c:0:7})

%global hug_lc 86e82de95e2a318589b718fef22eaeca1a3e3e04
%global hug_sc %(c=%{hug_lc}; echo ${c:0:7})

%global	jinja_lc b59d179defbc9fd6e6f426569f8430592e1a6a1b
%global jinja_sc %(c=%{jinja_lc}; echo ${c:0:7})

%global ntf_lc f7acffdc05b5db893daa8201f3ff85945da50fcb 
%global ntf_sc %(c=%{ntf_lc}; echo ${c:0:7})

%global	muxtheme_lc 7c59902f64dcd7ea356e891274b21144d1ea5948
%global muxtheme_sc %(c=%{muxtheme_lc}; echo ${c:0:7})

%global	salt_lc	6ca9e3500cc39dd417b411435d58a1b720b331cc
%global salt_sc %(c=%{salt_lc}; echo ${c:0:7})

%global supertab_lc 40fe711e088e2ab346738233dd5adbb1be355172 
%global supertab_sc %(c=%{supertab_lc}; echo ${c:0:7})

%global vimcolor_lc 9e7ab1cfec5d3db85aa1c4e87329fd869ecf94e9
%global vimcolor_sc %(c=%{vimcolor_lc}; echo ${c:0:7})

%global vp_lc e49f9e7e3fc041dab0e9a1de4b564b3ddd8f77aa
%global vp_sc %(c=%{vp_lc}; echo ${c:0:7})

%global vps_lc 0d1129e5cf1b0e3a90e923c3b5f40133bf153f7c
%global vps_sc %(c=%{vps_lc}; echo ${c:0:7})

%global vimde_lc 96d889bf7e39adf596fb12c1e039fa6dc3b87fa0
%global vimde_sc %(c=%{vimde_lc}; echo ${c:0:7})

%global	vimux_lc 37f41195e6369ac602a08ec61364906600b771f1
%global vimux_sc %(c=%{vimux_lc}; echo ${c:0:7})

%global vtnav_lc 44ba6fbe45895cd541ebfc87606add5c76e3829b
%global vtnav_sc %(c=%{vtnav_lc}; echo ${c:0:7})

%global	vundle_lc b255382d6242d7ea3877bf059d2934125e0c4d95
%global vundle_sc %(c=%{vundle_lc}; echo ${c:0:7})

%global yarp_lc b710bf4daccb603a423754794fb446e5fbb59576
%global yarp_sc %(c=%{yarp_lc}; echo ${c:0:7})

%global vas_version 0.1.7
%global deo_version 5.2

%undefine __brp_python_bytecompile
%undefine __brp_mangle_shebangs

Name:           vimde
Version:        2020.4.0
Release:        1.eog%{?dist}
Summary:        Simple Development Environment based on Vim and tmux


License:        Apache 2.0
URL:            https://github.com/c4t3l/vimde

Source0:        https://github.com/c4t3l/%{name}/archive/%{vimde_lc}/%{name}-%{vimde_sc}.tar.gz
Source1:	https://github.com/VundleVim/Vundle.vim/archive/%{vundle_lc}/Vundle.vim-%{vundle_sc}.tar.gz
Source2:	https://github.com/saltstack/salt-vim/archive/%{salt_lc}/salt_vim-%{salt_sc}.tar.gz
Source3:	https://github.com/Glench/Vim-Jinja2-Syntax/archive/%{jinja_lc}/Vim-Jinja2-Syntax-%{jinja_sc}.tar.gz
Source4:	https://github.com/benmills/vimux/archive/%{vimux_lc}/vimux-%{vimux_sc}.tar.gz
Source5:	https://github.com/jimeh/tmux-themepack/archive/%{muxtheme_lc}/tmux-themepack-%{muxtheme_sc}.tar.gz
Source6: 	https://github.com/flazz/vim-colorschemes/archive/%{vimcolor_lc}/vim-colorschemes-%{vimcolor_sc}.tar.gz
Source7:	https://github.com/vim-scripts/vim-auto-save/archive/%{vas_version}.tar.gz
Source8:	https://github.com/Shougo/deoplete.nvim/archive/%{deo_version}.tar.gz
Source9:	https://github.com/roxma/nvim-yarp/archive/%{yarp_lc}/nvim-yarp-%{yarp_sc}.tar.gz
Source10:	https://github.com/roxma/vim-hug-neovim-rpc/archive/%{hug_lc}/vim-hug-neovim-rpc-%{hug_sc}.tar.gz
Source11:	https://github.com/deoplete-plugins/deoplete-jedi/archive/%{deojedi_lc}/deoplete-jedi-%{deojedi_sc}.tar.gz
Source12:	https://github.com/ervandew/supertab/archive/%{supertab_lc}/supertab-%{supertab_sc}.tar.gz
Source13: 	https://github.com/low-ghost/nerdtree-fugitive/archive/%{ntf_lc}/nerdtree-fugitive-%{ntf_sc}.tar.gz
Source14: 	https://github.com/christoomey/vim-tmux-navigator/archive/%{vtnav_lc}/vim-tmux-navigator-%{vtnav_sc}.tar.gz
Source15: 	https://github.com/vim-pandoc/vim-pandoc/archive/%{vp_lc}/vim-pandoc-%{vp_sc}.tar.gz
Source16: 	https://github.com/vim-pandoc/vim-pandoc-syntax/archive/%{vps_lc}/vim-pandoc-syntax-%{vps_sc}.tar.gz


Requires:	ctags
Requires:	git
Requires:	python3 >= 3.8
Requires:	python3-msgpack
Requires:	python3-neovim
Requires:	python3-pudb
Requires:	tmux >= 2.9
Requires:	tmux-powerline
Requires:	vim-enhanced >= 8.0
Requires:	vim-nerdtree
Requires:	vim-powerline
Requires: 	pandoc
Requires: 	surf
Requires: 	vim-fugitive
Requires: 	vim-syntastic-python
Requires: 	vim-syntastic-yaml
Requires: 	wemux


%description
A simple Vim based IDE using vim plugins for Saltstack and RPM based development.
VimDE can easily be extended by adding new plugins and editing your local .vimderc
file.  


# We simply need to untar the sources and copy them to /usr/share/vimde/bundle
%prep
%autosetup -n %{name}-%{vimde_lc}
%autosetup -D -b 1 -n Vundle.vim-%{vundle_lc}
%autosetup -D -b 2 -n salt-vim-%{salt_lc}
%autosetup -D -b 3 -n Vim-Jinja2-Syntax-%{jinja_lc}
%autosetup -D -b 4 -n vimux-%{vimux_lc}
%autosetup -D -b 5 -n tmux-themepack-%{muxtheme_lc}
%autosetup -D -b 6 -n vim-colorschemes-%{vimcolor_lc}
%autosetup -D -b 7 -n vim-auto-save-%{vas_version}
%autosetup -D -b 8 -n deoplete.nvim-%{deo_version}
%autosetup -D -b 9 -n nvim-yarp-%{yarp_lc}
%autosetup -D -b 10 -n vim-hug-neovim-rpc-%{hug_lc}
%autosetup -D -b 11 -n deoplete-jedi-%{deojedi_lc}
%autosetup -D -b 12 -n supertab-%{supertab_lc}
%autosetup -D -b 13 -n nerdtree-fugitive-%{ntf_lc}
%autosetup -D -b 14 -n vim-tmux-navigator-%{vtnav_lc}
%autosetup -D -b 15 -n vim-pandoc-%{vp_lc}
%autosetup -D -b 16 -n vim-pandoc-syntax-%{vps_lc}


%install
mkdir -vp %{buildroot}%{_prefix}/bin
mkdir -vp %{buildroot}%{_sysconfdir}
mkdir -vp %{buildroot}%{_datarootdir}/doc
mkdir -vp %{buildroot}%{_datarootdir}/%{name}/bundle
mkdir -vp %{buildroot}%{_datarootdir}/tmuxde/plugins 

install -m 0755 %{_builddir}/%{name}-%{vimde_lc}/%{name} %{buildroot}%{_prefix}/bin/%{name}
install -m 0644 %{_builddir}/%{name}-%{vimde_lc}/%{name}.d/vimderc %{buildroot}%{_sysconfdir}/vimderc
install -m 0644 %{_builddir}/%{name}-%{vimde_lc}/%{name}.d/tmuxderc %{buildroot}%{_sysconfdir}/tmuxderc
cp -r %{_builddir}/Vundle.vim-%{vundle_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/Vundle.vim-%{vundle_lc}
cp -r %{_builddir}/salt-vim-%{salt_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/salt-vim-%{salt_lc}
cp -r %{_builddir}/Vim-Jinja2-Syntax-%{jinja_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/Vim-Jinja2-Syntax-%{jinja_lc}
cp -r %{_builddir}/vimux-%{vimux_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vimux-%{vimux_lc}
cp -r %{_builddir}/vim-colorschemes-%{vimcolor_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-colorschemes-%{vimcolor_lc}
cp -r %{_builddir}/vim-auto-save-%{vas_version} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-auto-save-%{vas_version}
cp -r %{_builddir}/deoplete.nvim-%{deo_version} %{buildroot}%{_datarootdir}/%{name}/bundle/deoplete.nvim-%{deo_version}
cp -r %{_builddir}/nvim-yarp-%{yarp_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/nvim-yarp-%{yarp_lc}
cp -r %{_builddir}/vim-hug-neovim-rpc-%{hug_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-hug-neovim-rpc-%{hug_lc}
cp -r %{_builddir}/deoplete-jedi-%{deojedi_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/deoplete-jedi-%{deojedi_lc}
cp -r %{_builddir}/supertab-%{supertab_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/supertab-%{supertab_lc}
cp -r %{_builddir}/nerdtree-fugitive-%{ntf_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/nerdtree-fugitive-%{ntf_lc}
cp -r %{_builddir}/vim-tmux-navigator-%{vtnav_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-tmux-navigator-%{vtnav_lc}
cp -r %{_builddir}/vim-pandoc-%{vp_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-pandoc-%{vp_lc}
cp -r %{_builddir}/vim-pandoc-syntax-%{vps_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-pandoc-syntax-%{vps_lc}
cp -r %{_builddir}/tmux-themepack-%{muxtheme_lc} %{buildroot}%{_datarootdir}/tmuxde/plugins/tmux-themepack-%{muxtheme_lc}

%files
%defattr(-,root,root,0755)
%{_datarootdir}/%{name}/
%{_datarootdir}/tmuxde/
%{_prefix}/bin/%{name}
%config %{_sysconfdir}/vimderc
%config %{_sysconfdir}/tmuxderc


%changelog
* Sat Apr 18 2020 Robby Callicotte <rcallicotte@gmail.com> - 2020.4.0-1.eog
- Initial build
