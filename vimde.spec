%global deojedi_lc 43058915007d92dc167b84dd5b8ada2d2a057a82
%global deojedi_sc %(c=%{deojedi_lc}; echo ${c:0:7})

%global hug_lc 93ae38792bc197c3bdffa2716ae493c67a5e7957
%global hug_sc %(c=%{hug_lc}; echo ${c:0:7})

%global jinja_lc b59d179defbc9fd6e6f426569f8430592e1a6a1b
%global jinja_sc %(c=%{jinja_lc}; echo ${c:0:7})

%global ntf_lc f7acffdc05b5db893daa8201f3ff85945da50fcb
%global ntf_sc %(c=%{ntf_lc}; echo ${c:0:7})

%global muxtheme_lc 7c59902f64dcd7ea356e891274b21144d1ea5948
%global muxtheme_sc %(c=%{muxtheme_lc}; echo ${c:0:7})

%global salt_lc 6ca9e3500cc39dd417b411435d58a1b720b331cc
%global salt_sc %(c=%{salt_lc}; echo ${c:0:7})

%global supertab_lc 40fe711e088e2ab346738233dd5adbb1be355172
%global supertab_sc %(c=%{supertab_lc}; echo ${c:0:7})

%global vp_lc e49f9e7e3fc041dab0e9a1de4b564b3ddd8f77aa
%global vp_sc %(c=%{vp_lc}; echo ${c:0:7})

%global vps_lc 0d1129e5cf1b0e3a90e923c3b5f40133bf153f7c
%global vps_sc %(c=%{vps_lc}; echo ${c:0:7})

%global vimux_lc f7c41607d9246ec4b6cc28587cce84d75d106e3e
%global vimux_sc %(c=%{vimux_lc}; echo ${c:0:7})

%global vtnav_lc 44ba6fbe45895cd541ebfc87606add5c76e3829b
%global vtnav_sc %(c=%{vtnav_lc}; echo ${c:0:7})

%global vundle_lc b255382d6242d7ea3877bf059d2934125e0c4d95
%global vundle_sc %(c=%{vundle_lc}; echo ${c:0:7})

%global yarp_lc b710bf4daccb603a423754794fb446e5fbb59576
%global yarp_sc %(c=%{yarp_lc}; echo ${c:0:7})

%global vas_version 0.1.7
%global deo_version 6.1


Name:           vimde
Version:        2024.5.0rc0
Release:        1%{?dist}
Summary:        Simple Development Environment based on Vim and tmux
License:        MIT and ASL2.0 and BSD3 and WTFPL2
URL:            https://github.com/c4t3l/vimde

Source0:        %{url}/archive/%{version}.tar.gz
Source1:        https://github.com/VundleVim/Vundle.vim/archive/%{vundle_lc}/Vundle.vim-%{vundle_sc}.tar.gz
Source2:        https://github.com/saltstack/salt-vim/archive/%{salt_lc}/salt_vim-%{salt_sc}.tar.gz
Source3:        https://github.com/Glench/Vim-Jinja2-Syntax/archive/%{jinja_lc}/Vim-Jinja2-Syntax-%{jinja_sc}.tar.gz
Source4:        https://github.com/preservim/vimux/archive/%{vimux_lc}/vimux-%{vimux_sc}.tar.gz
Source5:        https://github.com/jimeh/tmux-themepack/archive/%{muxtheme_lc}/tmux-themepack-%{muxtheme_sc}.tar.gz
Source7:        https://github.com/vim-scripts/vim-auto-save/archive/%{vas_version}.tar.gz
Source8:        https://github.com/Shougo/deoplete.nvim/archive/%{deo_version}.tar.gz
Source9:        https://github.com/roxma/nvim-yarp/archive/%{yarp_lc}/nvim-yarp-%{yarp_sc}.tar.gz
Source10:       https://github.com/roxma/vim-hug-neovim-rpc/archive/%{hug_lc}/vim-hug-neovim-rpc-%{hug_sc}.tar.gz
Source11:       https://github.com/deoplete-plugins/deoplete-jedi/archive/%{deojedi_lc}/deoplete-jedi-%{deojedi_sc}.tar.gz
Source12:       https://github.com/ervandew/supertab/archive/%{supertab_lc}/supertab-%{supertab_sc}.tar.gz
Source13:       https://github.com/low-ghost/nerdtree-fugitive/archive/%{ntf_lc}/nerdtree-fugitive-%{ntf_sc}.tar.gz
Source14:       https://github.com/christoomey/vim-tmux-navigator/archive/%{vtnav_lc}/vim-tmux-navigator-%{vtnav_sc}.tar.gz
Source15:       https://github.com/vim-pandoc/vim-pandoc/archive/%{vp_lc}/vim-pandoc-%{vp_sc}.tar.gz
Source16:       https://github.com/vim-pandoc/vim-pandoc-syntax/archive/%{vps_lc}/vim-pandoc-syntax-%{vps_sc}.tar.gz

BuildRequires:  python3-devel
Requires:       awesome-vim-colorschemes
Requires:       ctags
Requires:       git
Requires:       tmux >= 2.9
Requires:       tmux-powerline
Requires:       vim-ale
Requires:       vim-enhanced >= 8.0
Requires:       vim-nerdtree
Requires:       vim-powerline
Requires:       pandoc
Requires:       surf
Requires:       vim-fugitive
Requires:       wemux
BuildArch:      noarch

# Bundling is used here because none of the provided packages are versioned
# Most are not widely in use.
Provides:       bundled(vim-Vundle)
Provides:       bundled(salt-vim)
Provides:       bundled(Vim-Jinja2-Syntax)
Provides:       bundled(vim-vimux)
Provides:       bundled(tmux-themepack)
Provides:       bundled(vim-auto-save)
Provides:       bundled(deoplete-nvim)
Provides:       bundled(nvim-yarp)
Provides:       bundled(vim-hug-neovim-rpc)
Provides:       bundled(deoplete-jedi)
Provides:       bundled(vim-supertab)
Provides:       bundled(vim-nerdtree-fugitive)
Provides:       bundled(vim-tmux-navigator)
Provides:       bundled(vim-pandoc)
Provides:       bundled(vim-pandoc-syntax)


%description
A simple Vim based IDE using vim plugins for Saltstack and RPM based development.
VimDE can easily be extended by adding new plugins and editing your local .vimderc
file.


# We simply need to untar the sources and copy them to /usr/share/vimde/bundle
%prep
%autosetup -n %{name}-%{version}
%autosetup -D -b 1 -n Vundle.vim-%{vundle_lc}
%autosetup -D -b 2 -n salt-vim-%{salt_lc}
%autosetup -D -b 3 -n Vim-Jinja2-Syntax-%{jinja_lc}
%autosetup -D -b 4 -n vimux-%{vimux_lc}
%autosetup -D -b 5 -n tmux-themepack-%{muxtheme_lc}
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

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}

mkdir -vp %{buildroot}%{_datarootdir}/doc
mkdir -vp %{buildroot}%{_datarootdir}/%{name}/bundle
mkdir -vp %{buildroot}%{_datarootdir}/tmuxde/plugins

install -Dpm 0755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{_prefix}/bin/%{name}
install -Dpm 0644 %{_builddir}/%{name}-%{version}/%{name}.d/vimderc %{buildroot}%{_sysconfdir}/%{name}/vimderc
install -Dpm 0644 %{_builddir}/%{name}-%{version}/%{name}.d/tmuxderc %{buildroot}%{_sysconfdir}/%{name}/tmuxderc
cp -ar %{_builddir}/Vundle.vim-%{vundle_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/Vundle.vim
cp -ar %{_builddir}/salt-vim-%{salt_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/salt-vim
cp -ar %{_builddir}/Vim-Jinja2-Syntax-%{jinja_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/Vim-Jinja2-Syntax
cp -ar %{_builddir}/vimux-%{vimux_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vimux
cp -ar %{_builddir}/vim-auto-save-%{vas_version} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-auto-save
cp -ar %{_builddir}/deoplete.nvim-%{deo_version} %{buildroot}%{_datarootdir}/%{name}/bundle/deoplete.nvim
cp -ar %{_builddir}/nvim-yarp-%{yarp_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/nvim-yarp
cp -ar %{_builddir}/vim-hug-neovim-rpc-%{hug_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-hug-neovim-rpc
cp -ar %{_builddir}/deoplete-jedi-%{deojedi_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/deoplete-jedi
cp -ar %{_builddir}/supertab-%{supertab_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/supertab
cp -ar %{_builddir}/nerdtree-fugitive-%{ntf_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/nerdtree-fugitive
cp -ar %{_builddir}/vim-tmux-navigator-%{vtnav_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-tmux-navigator
cp -ar %{_builddir}/vim-pandoc-%{vp_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-pandoc
cp -ar %{_builddir}/vim-pandoc-syntax-%{vps_lc} %{buildroot}%{_datarootdir}/%{name}/bundle/vim-pandoc-syntax
cp -ar %{_builddir}/tmux-themepack-%{muxtheme_lc} %{buildroot}%{_datarootdir}/tmuxde/plugins/tmux-themepack


%check
%pyproject_check_import %{name}


%files -f %{pyproject_files}
%{_datarootdir}/%{name}/
%{_datarootdir}/tmuxde/
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/vimderc
%config(noreplace) %{_sysconfdir}/%{name}/tmuxderc


%changelog
* Sat May 25 2024 Robby Callicotte <rcallicotte@mailbox.org> - 2024.5.0rc0-1
- Updated to Release candidate

* Sun Aug 21 2022 Robby Callicotte <rcallicotte@mailbox.org> - 2022.8.0-1
- Rebased to new version

* Wed Jan 12 2022 Robby Callicotte <rcallicotte@mailbox.org> - 2022.1.0-1
- Initial build
