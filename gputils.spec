Summary:	Tools for the Microchip (TM) PIC microcontrollers
Summary(pl.UTF-8):	Narzędzia dla mikrokontrolerów PIC Microchip(TM)
Name:		gputils
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/gputils/%{name}-%{version}.tar.gz
# Source0-md5:	175dedeb141b4a4609a70262847257e4
URL:		http://gputils.sourceforge.net/
BuildRequires:	flex >= 2.5.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for the Microchip(TM) PIC microcontrollers.

%description -l pl.UTF-8
Narzędzia dla mikrokontrolerów PIC Microchip(TM).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/html-help
%attr(755,root,root) %{_bindir}/gpasm
%attr(755,root,root) %{_bindir}/gpdasm
%attr(755,root,root) %{_bindir}/gplib
%attr(755,root,root) %{_bindir}/gplink
%attr(755,root,root) %{_bindir}/gpstrip
%attr(755,root,root) %{_bindir}/gpvc
%attr(755,root,root) %{_bindir}/gpvo
%{_datadir}/%{name}
%{_mandir}/man1/gpasm.1*
%{_mandir}/man1/gpdasm.1*
%{_mandir}/man1/gplib.1*
%{_mandir}/man1/gplink.1*
%{_mandir}/man1/gpstrip.1*
%{_mandir}/man1/gputils.1*
%{_mandir}/man1/gpvc.1*
%{_mandir}/man1/gpvo.1*
%{_mandir}/fr/man1/gpasm.1*
%{_mandir}/fr/man1/gpdasm.1*
%{_mandir}/fr/man1/gplib.1*
%{_mandir}/fr/man1/gplink.1*
%{_mandir}/fr/man1/gpstrip.1*
%{_mandir}/fr/man1/gputils.1*
%{_mandir}/fr/man1/gpvc.1*
%{_mandir}/fr/man1/gpvo.1*
