%define rname WoeUSB
%define debug_package %{nil}

Summary:	Creates Windows USB stick installer from a Windows DVD or image
Name:		woeusb
Version:	5.2.4
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		https://github.com/slacka/WoeUSB
Source0:	https://github.com/WoeUSB/WoeUSB/archive/v%{version}/%{rname}-%{version}.tar.gz
Source1:	trad.mo
#Patch0:		russian-translated-shortcut-3.2.12.patch
BuildRequires:	wxgtku3.0-devel 
BuildRequires:	imagemagick
BuildRequires:	jpeg-devel

%description
This package contains two programs:

 o woeusb: A command-line utility that enables you to create your own bootable
Windows installation USB storage device from an existing Windows
Installation disc or disk image

 o woeusbgui: A GUI wrapper of woeusb based on WxWidgets

Supported images:

Windows Vista, Windows 7, Window 8.x, Windows 10. All languages and any version
(home, pro...) and Windows PE are supported.

Supported bootmodes:

Legacy/MBR-style/IBM PC compatible bootmode
Native UEFI booting is supported for Windows 7 and later images
(limited to the FAT filesystem as the target)

%files -f %{name}.lang

%{_bindir}/%{name}
%{_bindir}/%{name}gui
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/%{name}gui.*
%{_datadir}/pixmaps/%{name}gui-icon.png
%{_datadir}/woeusb/data/*
%{_datadir}/woeusb/locale/fr/LC_MESSAGES/wxstd.mo
%{_datadir}/locale/ru/LC_MESSAGES/trad.mo
%{_datadir}/applications/%{name}gui.desktop

#---------------------------------------------------------------

%prep
%setup -qn %{rname}-%{version}
#patch0 -p1

%build
autoreconf -fiv
%configure2_5x \
	--enable-shared \
	--disable-static \
	--disable-dependency-tracking
%make

%install
%makeinstall_std

#added russian translate
install -D %{SOURCE1} %{buildroot}%{_datadir}/locale/ru/LC_MESSAGES/trad.mo

%find_lang %{name}

