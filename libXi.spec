# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       libXi
Summary:    X.Org X11 libXi runtime library
Version:    1.5.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXi.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(inputproto) >= 2.0.99.1


%description
%{summary}.



%package devel
Summary:    Development components for the libXi library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.1.0
%doc COPYING
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
%{_datadir}/doc/libXi/*
%{_mandir}/man3/*
# << files devel

