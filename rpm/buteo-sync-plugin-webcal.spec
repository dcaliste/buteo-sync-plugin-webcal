Name:       buteo-sync-plugin-webcal
Summary:    Syncs online calendar resource in ICS format
Version:    0.0.7
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        https://git.merproject.org/dcaliste/buteo-sync-plugin-webcal
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(libmkcal-qt5)
BuildRequires:  pkgconfig(libkcalcoren-qt5)
BuildRequires:  pkgconfig(buteosyncfw5)
Requires: buteo-syncfw-qt5-msyncd

%description
A Buteo plugin which syncs a ICS resource online

%files
%defattr(-,root,root,-)
#out-of-process-plugin
/usr/lib/buteo-plugins-qt5/oopp/webcal-client
#in-process-plugin
#/usr/lib/buteo-plugins-qt5/libwebcal-client.so
%config %{_sysconfdir}/buteo/profiles/sync/webcal-sync.xml
%config %{_sysconfdir}/buteo/profiles/client/webcal.xml

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 "DEFINES+=BUTEO_OUT_OF_PROCESS_SUPPORT"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post
systemctl-user try-restart msyncd.service || :
