%global goipath  github.com/alcortesm/tgz
%global commit   9c5fe88206d7765837fed3732a42ef88fc51f1a1

%global common_description %{expand:
A Go library to extract tgz files to temporal directories.}

%gometa

Name: %{goname}
Version: 0
Release: 0.4%{?dist}
Summary: Extract tgz files to temporal directories
License: MIT
URL: %{gourl}
Source0: %{gosource}

# https://github.com/alcortesm/tgz/pull/3
Patch0: 0001-fix-format-error.patch

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%forgesetup
%patch0 -p1

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.201804036git9c5fe88
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.3.201804036git9c5fe88
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git9c5fe88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Dominik Mierzejewski <dominik@greysector.net> - 0-0.1.201804036git9c5fe88
- First package for Fedora
