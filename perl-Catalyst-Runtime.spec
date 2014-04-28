%define	upstream_name    Catalyst-Runtime
%define upstream_version 5.90061

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
Release:	1
Epoch:		1

Summary:	The Elegant MVC Web Application Framework

License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires: perl(Plack::Middleware::ReverseProxy)
BuildRequires: perl(Safe::Isa)
BuildRequires: perl(Carp::Always)
BuildRequires: perl(Test::Without::Module)
BuildRequires: perl(Test::Tester)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::MockTime)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::Deep::NoTest)
BuildRequires: perl(Stream::Buffered)
BuildRequires: perl(Plack::Test)
BuildRequires: perl(Plack::Request)
BuildRequires: perl(Plack::Middleware)
BuildRequires: perl(Plack::Loader)
BuildRequires: perl(Plack::Builder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(JSON::MaybeXS)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(HTTP::Message::PSGI)
BuildRequires: perl(File::ShareDir::Install)
BuildRequires: perl(Cpanel::JSON::XS)
BuildRequires: perl(Apache::LogFormat::Compiler)
BuildRequires: perl(CGI::Struct)
BuildRequires: perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires: perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires: perl(Plack::Middleware::MethodOverride)
BuildRequires: perl(Plack::Test::ExternalServer)
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
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Encode
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

