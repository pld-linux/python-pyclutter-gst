Summary:	Python bindings for the Clutter-GStreamer integration library
Summary(pl.UTF-8):	Dowiązania Pythona do biblioteki integrującej Clutter-GStreamer
Name:		python-pyclutter-gst
Version:	1.0.0
Release:	1
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	http://source.clutter-project.org/sources/pyclutter-gst/1.0/pyclutter-gst-%{version}.tar.bz2
# Source0-md5:	b1cc99a70042bb91ad75937405ed64d9
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gst-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-gstreamer-devel >= 0.10
BuildRequires:	python-pyclutter-devel >= 1.0.0
BuildRequires:	python-pygobject-devel >= 2.12.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	clutter >= 1.0.0
Requires:	clutter-gst >= 1.0.0
Requires:	python-gstreamer >= 0.10
Requires:	python-pyclutter >= 1.0.0
Requires:	python-pygobject >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the Clutter-GStreamer integration library.

%description -l pl.UTF-8
Dowiązania Pythona do biblioteki integrującej Clutter-GStreamer.

%package devel
Summary:	Development files for Cutter-GStremer Python binding
Summary(pl.UTF-8):	Pliki programistyczne wiązania Pythona do Clutter-GStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.0.0
Requires:	clutter-gst-devel >= 1.0.0
Requires:	python-gstreamer-devel >= 0.10
Requires:	python-pyclutter-devel >= 1.0.0
Requires:	python-pygobject-devel >= 2.12.1

%description devel
Development files for Cutter-GStremer Python binding.

%description devel -l pl.UTF-8
Pliki programistyczne wiązania Pythona do Clutter-GStreamer.

%prep
%setup -q -n pyclutter-gst-%{version}

%build
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/cluttergst/*.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{py_sitedir}/cluttergst
%attr(755,root,root) %{py_sitedir}/cluttergst/_cluttergst.so
%{py_sitedir}/cluttergst/*.py[co]
%{_datadir}/pyclutter

%files devel
%defattr(644,root,root,755)
%{_datadir}/pyclutter/1.0/defs/cluttergst*.defs
%{_pkgconfigdir}/pyclutter-gst-1.0.pc
