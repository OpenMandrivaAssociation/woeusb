# Upgrading this package involves, changing the release tag
# as well as patching it.
# To create the patch, 1) git clone repository 2) ptr start
# 3) ./setup-development-environment 4) ptr diff
# The above cannot be done in the spec, use the patch to update
# package (- mjack).

Name:			woeusb
Version:		3.1.4
Release:		%mkrel 1
Summary:		Create a Windows USB from a real Windows DVD or image
License:		GPLv3
Group:			Archiving/Other
URL:			https://github.com/slacka/WoeUSB
Source0:		https://github.com/slacka/WoeUSB/archive/v%{version}/WoeUSB-%{version}.tar.gz
Patch0:			woeusb-3.1.4-setup-development-environment-release.patch
BuildRequires:		wxgtku3.0-devel

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


#------------------------------------------------------------
%prep

%setup -q -n'WoeUSB-%{version}'
%apply_patches

%build

autoreconf --force --install
%configure2_5x \
	--enable-shared \
	--disable-static

%make

%install
%makeinstall_std
%find_lang %{name}

#------------------------------------------------------------
%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}gui
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/%{name}gui.*
%{_datadir}/pixmaps/%{name}gui-icon.png
%{_datadir}/%{name}/data/*
%{_datadir}/applications/%{name}gui.desktop
