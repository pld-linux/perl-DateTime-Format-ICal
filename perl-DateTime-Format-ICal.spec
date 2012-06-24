#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-ICal
Summary:	DateTime::Format::ICal - Parse and format iCal datetime and duration strings
Summary(pl):	DateTime::Format::ICal - analiza i formatowanie �a�cuch�w czas�w i okres�w iCal
Name:		perl-DateTime-Format-ICal
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/DateTime-Format-ICal-%{version}.tar.gz
# Source0-md5:	b0be692f3a84f2a7f73a39220ec69a52
URL:		http://search.cpan.org/dist/DateTime-Format-ICal/
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

%description -l pl
Ten modu� rozumie formaty daty/czasu i okres�w ICal zgodnie z
definicj� w RFC 2445. Mo�e by� u�ywany do analizy tych format�w w celu
tworzenia odpowiednich obiekt�w.

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
%doc Changes README
%{perl_vendorlib}/DateTime/Format/*.pm
%{_mandir}/man3/*
