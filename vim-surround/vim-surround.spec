%global vimfiles_root %{_datadir}/vim/vimfiles

Name:             vim-surround
Version:          2.1
Release:          1%{?dist}
Summary:          mappings to delete, change and add such surroundings in pairs

Group:            Applications/Editors

License:          Charityware
URL:              http://www.vim.org/scripts/script.php?script_id=1697
Source0:          https://github.com/tpope/%{name}/archive/v%{version}.tar.gz

Requires:         vim-filesystem
Requires(post):   vim
Requires(postun): vim

BuildArch:      noarch

%description
Surround.vim is all about "surroundings": parentheses, brackets, quotes, XML
tags, and more. The plugin provides mappings to easily delete, change and add
such surroundings in pairs.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,plugin} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc %{vimfiles_root}/doc/
%{vimfiles_root}/plugin/

%changelog
* Fri Apr 01 2016 Marc Deop <marc@marcdeop.com> - 2.1
- Initial package.
