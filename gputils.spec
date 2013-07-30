
Summary:	Tools for the Microchip (TM) PIC microcontrollers
Name:		gputils
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gputils/%{name}-%{version}.tar.gz
# Source0-md5:	4332391ce058c636d6c15d05d4cecd86
URL:		http://gputils.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for the Microchip (TM) PIC microcontrollers.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/html-help
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/%{name}
