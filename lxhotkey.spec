#
# Conditional build:
%bcond_without	gtk3	# use GTK+3 instead of GTK+2

Summary:	A lightweight global keyboard shortcuts configurator
Summary(pl.UTF-8):	Lekki konfigurator globalnych skrótów klawiaturowych
Name:		lxhotkey
Version:	0.1.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	8c932c568fa822f3e1bf4ce23f00d881
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	libunistring-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18.0}
Requires:	libfm >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A lightweight global keyboard shortcuts configurator.

%description -l pl.UTF-8
Lekki konfigurator globalnych skrótów klawiaturowych.

%package devel
Summary:	Header file for lxhotkey plugins
Summary(pl.UTF-8):	Plik nagłówkowy dla wtyczek programu lxhotkey
Group:		Development/Libraries
Requires:	libfm-devel >= 1.2.0

%description devel
Header file for lxhotkey plugins.

%description devel -l pl.UTF-8
Plik nagłówkowy dla wtyczek programu lxhotkey.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-gtk=%{?with_gtk3:3}%{!?with_gtk3:2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/lxhotkey
%dir %{_libdir}/lxhotkey
%attr(755,root,root) %{_libdir}/lxhotkey/gtk.so
%attr(755,root,root) %{_libdir}/lxhotkey/ob.so
%{_desktopdir}/lxhotkey-gtk.desktop
%{_mandir}/man1/lxhotkey.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxhotkey
%{_pkgconfigdir}/lxhotkey.pc
