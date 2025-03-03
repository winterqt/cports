pkgname = "acpid"
pkgver = "2.0.34"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "automake"]
makedepends = ["linux-headers"]
pkgdesc = "ACPI Daemon (acpid) With Netlink Support"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/acpid2"
source = f"https://downloads.sourceforge.net/sourceforge/acpid2/{pkgname}-{pkgver}.tar.xz"
sha256 = "2d095c8cfcbc847caec746d62cdc8d0bff1ec1bc72ef7c674c721e04da6ab333"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_service(self.files_path / "acpid")
    self.install_dir("etc/acpi/events", empty=True)
