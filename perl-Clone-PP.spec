%define upstream_name	 Clone-PP

Name:		perl-%{upstream_name}
Version:	1.08
Release:	2

Summary:	Recursively copy Perl datatypes
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Clone-PP-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

%prep
%autosetup -n %{upstream_name}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Clone
