
Summary:	Tools for the Microchip (TM) PIC microcontrollers
Name:		gputils
Version:	0.13.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gputils/%{name}-%{version}.tar.gz
# Source0-md5:	a95744578c6f7d616235434be1dc3603
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/%{name}
