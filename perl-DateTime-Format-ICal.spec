#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-ICal
Summary:	DateTime::Format::ICal - Parse and format iCal datetime and duration strings
Summary(pl.UTF-8):	DateTime::Format::ICal - analiza i formatowanie łańcuchów czasów i okresów iCal
Name:		perl-DateTime-Format-ICal
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17bb64bfb515f2db365ba5bb5a68a143
URL:		http://search.cpan.org/dist/DateTime-Format-ICal/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime >= 0.17
BuildRequires:	perl-DateTime-Event-ICal >= 0.03
BuildRequires:	perl-DateTime-Set >= 0.1
BuildRequires:	perl-DateTime-TimeZone >= 0.22
BuildRequires:	perl-Params-Validate >= 0.59
%endif
Requires:	perl-DateTime >= 0.28-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module understands the ICal date/time and duration formats, as
defined in RFC 2445. It can be used to parse these formats in order to
create the appropriate objects.

%description -l pl.UTF-8
Ten moduł rozumie formaty daty/czasu i okresów ICal zgodnie z
definicją w RFC 2445. Może być używany do analizy tych formatów w celu
tworzenia odpowiednich obiektów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*
