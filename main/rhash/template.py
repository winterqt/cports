pkgname = "rhash"
pkgver = "1.4.3"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--enable-openssl",
    "--disable-openssl-runtime",
    "--enable-lib-static",
    "--enable-lib-shared",
]
make_build_target = "all"
make_build_args = ["lib-shared"]
make_install_target = "install"
make_install_args = ["install-lib-shared"]
makedepends = ["openssl-devel"]
pkgdesc = "Utility for computing hash sums and creating magnet links"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/rhash/RHash"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1e40fa66966306920f043866cbe8612f4b939b033ba5e2708c3f41be257c8a3e"


def init_configure(self):
    self.configure_args += [
        "--cc=" + self.get_tool("CC"),
        "--ar=" + self.get_tool("AR"),
        "--extra-cflags=" + self.get_cflags(shell=True),
        "--extra-ldflags=" + self.get_ldflags(shell=True),
    ]


def post_install(self):
    self.make.invoke(
        None,
        [
            "-C",
            "librhash",
            "install-lib-headers",
            "PREFIX=/usr",
            "DESTDIR=" + str(self.chroot_destdir),
        ],
    )

    self.install_link("librhash.so.0", "usr/lib/librhash.so")

    self.install_license("COPYING")


@subpackage("rhash-devel")
def _devel(self):
    return self.default_devel()
