%define	upstream_name    Catalyst-Runtime
%define upstream_version 5.80030

# remove circular dependency: catalyst::helper is provided by
# catalyst-devel, which itself requires catalyst-runtime to be build.
# moreover, this dependency is only used in an example script, so we do
# not loose anything by removing this dependency
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Catalyst::Helper\\)'
%else
%define _requires_exceptions perl.Catalyst::Helper.
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	The Elegant MVC Web Application Framework
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(Carp)
BuildRequires:	perl(CGI::Simple::Cookie)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::C3::Adopt::NEXT)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(File::Modified)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTTP::Body) >= 0.60.0
BuildRequires:	perl(HTTP::Headers) >= 1.640.0
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::AsCGI) >= 0.500.0
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Module::Pluggable) >= 3.10.0
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(MooseX::MethodAttributes::Inheritable)
BuildRequires:	perl(MooseX::Role::WithOverloading) >= 0.30.0
BuildRequires:	perl(MooseX::Types::Common::Numeric)
BuildRequires:	perl(MooseX::Types::LoadableClass)
BuildRequires:	perl(Path::Class) >= 0.90.0
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(Text::SimpleTable) >= 0.30.0
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Tree::Simple) >= 1.150.0
BuildRequires:	perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:	perl(URI) >= 1.350.0
BuildRequires:	perl(YAML) >= 0.550.0
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl-devel

BuildArch:	noarch

# (misc) not auto-detected; as it's on a line with whitespace, it's not taken
# in account by perl.req
Requires:	perl(HTTP::Request::AsCGI) >= 0.500.0
Requires:	perl(MooseX::Emulate::Class::Accessor::Fast)
%rename perl-Catalyst

%description
Catalyst is an elegant web application framework, extremely flexible yet
extremely simple. It's similar to Ruby on Rails, Spring (Java) and Maypole,
upon which it was originally based.

Catalyst follows the Model-View-Controller (MVC) design pattern, allowing you
to easily separate concerns, like content, presentation, and flow control, into
separate modules. This separation allows you to modify code that handles one
concern without affecting code that handles the others. Catalyst promotes the
re-use of existing Perl modules that already handle common web application
concerns well.

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
%doc Changes
%{perl_vendorlib}/Catalyst*
%{_bindir}/catalyst.pl
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:5.800.300-2mdv2011.0
+ Revision: 680768
- mass rebuild

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:5.800.300-1mdv2011.0
+ Revision: 628698
- update to new version 5.80030

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.290-1mdv2011.0
+ Revision: 597214
- update to 5.80029

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.270-1mdv2011.0
+ Revision: 575592
- update to 5.80027

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.250-1mdv2011.0
+ Revision: 569944
- update to 5.80025

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.240-1mdv2011.0
+ Revision: 553070
- update to 5.80024

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.220-1mdv2010.1
+ Revision: 528760
- update to 5.80022

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.210-1mdv2010.1
+ Revision: 514103
- update to 5.80021

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.200-1mdv2010.1
+ Revision: 501143
- update to 5.80020

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.190-1mdv2010.1
+ Revision: 497909
- update to 5.80019
- patch no more used, removing it

* Wed Jan 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.180-1mdv2010.1
+ Revision: 490489
- update to 5.80018

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.170-1mdv2010.1
+ Revision: 488840
- update to 5.80017

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.160-1mdv2010.1
+ Revision: 477623
- update to 5.80016

* Fri Dec 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.150-1mdv2010.1
+ Revision: 473315
- adding missing buildrequires:
- adding missing buildrequires:
- update to 5.80015

* Mon Nov 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.140-1mdv2010.1
+ Revision: 469269
- update buildrequires:
- update buildrequires: version
- update to 5.80014

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.130-1mdv2010.0
+ Revision: 444317
- update to 5.80013

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.120-1mdv2010.0
+ Revision: 436569
- update to 5.80012

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.110-1mdv2010.0
+ Revision: 421138
- update to 5.80011

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.70-1mdv2010.0
+ Revision: 393130
- adding missing buildrequires:
- adding missing buildrequires:
- update to 5.80007

* Wed Jun 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:5.800.50-3mdv2010.0
+ Revision: 388887
- fix dependencies

* Sun Jun 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.50-2mdv2010.0
+ Revision: 385875
- removing circular dependency found in an example script

* Fri Jun 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1:5.800.50-1mdv2010.0
+ Revision: 385484
- removed one buildrequires: too much
- removed on buildrequires: too much
- updating buildrequires:
- forgot to add the new tarball
- adding an epoch: to force new version scheme

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 5.71001-1mdv2010.0
+ Revision: 376155
- update to 5.71001

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.7015-1mdv2009.1
+ Revision: 294621
- update to new version 5.7015

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 5.7014-2mdv2009.0
+ Revision: 268395
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.7014-1mdv2009.0
+ Revision: 212200
- update to new version 5.7014

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.7013-1mdv2009.0
+ Revision: 209319
- update to new version 5.7013

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.7012-1mdv2008.1
+ Revision: 132044
- update to new version 5.7012

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.7011-1mdv2008.1
+ Revision: 104515
- update to new version 5.7011

* Tue Aug 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.7010-1mdv2008.0
+ Revision: 72791
- update to new version 5.7010

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.7008-1mdv2008.0
+ Revision: 63922
- update to new version 5.7008

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 5.7007-1mdv2008.0
+ Revision: 19703
- 5.7007


* Tue Jan 30 2007 Scott Karns <scottk@mandriva.org> 5.7006-1mdv2007.0
+ Revision: 115452
- Restored perl(YAML) build dependency
- Removed source for previous version
- Updated to CPAN version 5.7006
- Patched to disable Module::Install's auto_install method

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Catalyst-Runtime

* Wed Sep 27 2006 Scott Karns <scottk@mandriva.org> 5.7003-1mdv2007.0
- CPAN 5.7003 release

* Thu Aug 03 2006 Scott Karns <scottk@mandriva.org> 5.7001-1mdv2007.0
- CPAN 5.7001 release

* Sun Jul 09 2006 Scott Karns <scottk@mandriva.org> 5.7000-1mdv2007.0
- CPAN 5.7000 release

* Sat Jul 01 2006 Scott Karns <scottk@mandriva.org> 5.70.03-2mdv2007.0
- Added BuildRequires YAML

* Fri Jun 30 2006 Scott Karns <scottk@mandriva.org> 5.70.03-1mdv2007.0
- First Mandriva release: 5.70_03 CPAN developer release

