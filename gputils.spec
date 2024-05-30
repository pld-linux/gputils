Summary:	Tools for the Microchip (TM) PIC microcontrollers
Summary(pl.UTF-8):	Narzędzia dla mikrokontrolerów PIC Microchip(TM)
Name:		gputils
Version:	1.5.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/gputils/%{name}-%{version}.tar.bz2
# Source0-md5:	6b27bea5f67b2bc6f1c7b91c75ddc462
URL:		https://gputils.sourceforge.io/
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
%doc AUTHORS ChangeLog README TODO doc/html-help
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
%lang(fr) %{_mandir}/fr/man1/gpasm.1*
%lang(fr) %{_mandir}/fr/man1/gpdasm.1*
%lang(fr) %{_mandir}/fr/man1/gplib.1*
%lang(fr) %{_mandir}/fr/man1/gplink.1*
%lang(fr) %{_mandir}/fr/man1/gpstrip.1*
%lang(fr) %{_mandir}/fr/man1/gputils.1*
%lang(fr) %{_mandir}/fr/man1/gpvc.1*
%lang(fr) %{_mandir}/fr/man1/gpvo.1*
