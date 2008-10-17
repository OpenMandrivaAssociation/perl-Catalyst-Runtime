%define	module		Catalyst-Runtime
%define	modprefix	Catalyst
%define	name		perl-%{module}

%define	version		5.7015
%define	realversion	%{version}

%define	release		%mkrel 1

Summary:	The Elegant MVC Web Application Framework
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{realversion}.tar.bz2
Patch0:		Catalyst-Runtime-noauto_instal.patch
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Carp)
BuildRequires:	perl(CGI::Simple::Cookie)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(File::Modified)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTTP::Body) >= 0.6
BuildRequires:	perl(HTTP::Headers) >= 1.64
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::AsCGI) >= 0.5
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Module::Pluggable) >= 3.01
BuildRequires:	perl(NEXT)
BuildRequires:	perl(Path::Class) >= 0.09
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(Text::SimpleTable) >= 0.03
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Tree::Simple) >= 1.15
BuildRequires:	perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:	perl(URI) >= 1.35
BuildRequires:	perl(YAML) >= 0.55
Requires:	perl >= 5.8.1
# (misc) not auto-detected; as it's on a line with whitespace, it's not taken
# in account by perl.req
Requires:	perl-HTTP-Request-AsCGI >= 0.5
Provides:	perl-Catalyst = %{version}-%{release}
Obsoletes:	perl-Catalyst
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot
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
%setup -q -n %{module}-%{realversion}
%patch0 -p0 -b .noauto_install

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}*
%{_bindir}/catalyst.pl
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


