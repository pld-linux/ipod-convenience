Summary:	iPod Convenience: A suite of scripts for 7th Generation iPods
Summary(pl.UTF-8):	iPod Convenience - zestaw skryptów do iPodów 7. generacji
Name:		ipod-convenience
Version:	0.9
Release:	1
License:	GPL v3
Group:		Applications/Communications
# bzr get lp:~glen666/ipod-convenience/pld-patches ipod-convenience.tar.bz2
# tar -cjf ipod-convenience.tar.bz2 --exclude=.bzr ipod-convenience.tar.bz2
Source0:	%{name}.tar.bz2
# Source0-md5:	7ecfb8e400d4d958e51a8cb6007ce430
URL:		https://launchpad.net/ipod-convenience
BuildRequires:	sed >= 4.0
Requires:	ping
Requires:	sshfs-fuse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apple's 7th Generation family of iPods (Touch & iPhone) can no longer
be synced via USB in Linux. Instead, the devices need to be synced
over a wireless connection. In order for the devices to work in the
existing applications, several things need to be taken into account
that aren't normally a concern with earlier generations.

%description -l pl.UTF-8
Rodzina urządzeń iPod firmy Apple 7. generacji (iPod Touch i iPhone)
nie może być już synchronizowana pod Linuksem po USB. Zamiast tego
urządzenia te muszą być synchronizowane po połączeniu bezprzewodowym.
Aby działały z istniejącymi aplikacjami, trzeba wziąć pod uwagę cechy,
które nie miały znaczenia we wcześniejszych generacjach.

%prep
%setup -q -n %{name}
find -type f | xargs grep -l /etc/default/ipod-convenience | xargs %{__sed} -i -e 's,/etc/default/ipod-convenience,/etc/sysconfig/ipod-convenience,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1,/etc/sysconfig}
cp -a *.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a etc/default/%{name} $RPM_BUILD_ROOT/etc/sysconfig

# install first script, make rest as symlinks
install usr/share/%{name}/mount-umount $RPM_BUILD_ROOT%{_bindir}/iphone-mount
ln -s iphone-mount $RPM_BUILD_ROOT%{_bindir}/iphone-umount
ln -s iphone-mount $RPM_BUILD_ROOT%{_bindir}/ipod-touch-mount
ln -s iphone-mount $RPM_BUILD_ROOT%{_bindir}/ipod-touch-umount

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ipod-convenience
%attr(755,root,root) %{_bindir}/iphone-mount
%attr(755,root,root) %{_bindir}/iphone-umount
%attr(755,root,root) %{_bindir}/ipod-touch-mount
%attr(755,root,root) %{_bindir}/ipod-touch-umount
%{_mandir}/man1/iphone-mount.1*
%{_mandir}/man1/iphone-umount.1*
%{_mandir}/man1/ipod-touch-mount.1*
%{_mandir}/man1/ipod-touch-umount.1*
