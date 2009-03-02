#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	AttributeHelpers
Summary:	MooseX::AttributeHelpers - Extend your attribute interfaces
#Summary(pl.UTF-8):	
Name:		perl-MooseX-AttributeHelpers
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f8589c9f8b246bb6ebff245a274b62b
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/MooseX-AttributeHelpers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.45
BuildRequires:	perl-Test-Exception >= 0.21
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
While Moose attributes provide you with a way to name your accessors,
readers, writers, clearers and predicates, this library provides commonly
used attribute helper methods for more specific types of data.

As seen in the /SYNOPSIS, you specify the extension via the 
metaclass parameter. Available meta classes are:



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/AttributeHelpers
%{_mandir}/man3/*
