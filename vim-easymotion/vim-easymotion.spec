%global vimfiles_root %{_datadir}/vim/vimfiles

Name:             vim-easymotion
Version:          3.0.1
Release:          1%{?dist}
Summary:          EasyMotion provides a simpler way to use some motions in vim.

Group:            Applications/Editors

License:          MIT
URL:              https://github.com/easymotion/vim-easymotion
Source0:          https://github.com/easymotion/%{name}/archive/v%{version}.tar.gz

Requires:         vim-filesystem
Requires(post):   vim
Requires(postun): vim

BuildArch:      noarch

%description
EasyMotion provides a much simpler way to use some motions in vim. It takes the
<number> out of <number>w or <number>f{char} by highlighting all possible
choices and allowing you to press one key to jump directly to the target.

When one of the available motions is triggered, all visible text preceding or
following the cursor is faded, and motion targets are highlighted.

EasyMotion is triggered by the provided mappings. This readme only covers the
basics; please refer to :help easymotion.txt to see all the available mappings.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {autoload,doc,plugin} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc %{vimfiles_root}/doc/
%{vimfiles_root}/autoload/
%{vimfiles_root}/plugin/

%changelog
* Sun Apr 03 2016 Marc Deop <marc@marcdeop.com> - 3.0.1
- Initial package.
