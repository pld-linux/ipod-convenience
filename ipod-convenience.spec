Summary:	iPod Convenience: A suite of scripts for 7th Generation iPods
Name:		ipod-convenience
Version:	0.5
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	ipod.tar.bz2
# Source0-md5:	cf62f438b820ef0da4d7f2f3ed49a5a8
URL:		https://launchpad.net/ipod-convenience
BuildRequires:	sed >= 4.0
Requires:	sshfs-fuse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apple's 7th Generation family of iPods (Touch & iPhone) can no longer
be synced via USB in Linux. Instead, the devices need to be synced
over a wireless connection. In order for the devices to work in the
existing applications, several things need to be taken into account
that aren't normally a concern with earlier generations.

%prep
%setup -q -n ipod
find -type f | xargs grep -l /etc/default/ipod-convenience | xargs sed -i -e 's,/etc/default/ipod-convenience,/etc/sysconfig/ipod-convenience,'

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
