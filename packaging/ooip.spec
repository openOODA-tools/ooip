Name:           ooip
Version:        0.1.0
Release:        1%{?dist}
Summary:        Inspects and configures IP addresses, interfaces, and link layer states.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooip
Source0:        ooip-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooip is a sovereign, capability-bounded IP ADDRESS TOOL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooip
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooip-uninstall

%files
/usr/bin/ooip
/usr/bin/ooip-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
