%define upstream_name	 Clone-PP%define upstream_version 1.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Recursively copy Perl datatypes
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Clone/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a general-purpose clone function to make deep
copies of Perl data structures. It calls itself recursively to copy
nested hash, array, scalar and reference types, including tied
variables and objects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Clone


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 680834
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 406317
- rebuild using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.02-2mdv2009.0
+ Revision: 136685
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdv2008.0
+ Revision: 86183
- rebuild


* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 1.02-1mdk
- Initial MDV release


