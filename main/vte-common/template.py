pkgname = "vte-common"
pkgver = "0.72.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Db_ndebug=false",
    "-D_systemd=false",
    "-Dgir=true",
    "-Dvapi=true",
    "-Dgtk4=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-tiny-devel",
    "gperf",
    "gobject-introspection",
    "vala",
    "bash",
]
makedepends = [
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "pcre2-devel",
    "vala-devel",
    "pango-devel",
    "fribidi-devel",
    "icu-devel",
    "zlib-devel",
    "linux-headers",
]
pkgdesc = "Gtk terminal widget (common files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = (
    f"https://gitlab.gnome.org/GNOME/vte/-/archive/{pkgver}/vte-{pkgver}.tar.gz"
)
sha256 = "c42a6cf407216439c87ca56109b013d7c640cbb10dafea4a093a9a21377b6698"
# assert in meson
options = ["!lto", "!cross"]


@subpackage("vte-gtk3")
def _gtk3(self):
    self.pkgdesc = "Gtk+3 terminal widget"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/vte-2.91",
        "usr/lib/libvte-2.91.so.*",
        "usr/lib/girepository-1.0/Vte-2.91.typelib",
    ]


@subpackage("vte-gtk4")
def _gtk4(self):
    self.pkgdesc = "Gtk4 terminal widget"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/vte-2.91-gtk4",
        "usr/lib/libvte-2.91-gtk4.so.*",
        "usr/lib/girepository-1.0/Vte-3.91.typelib",
    ]


@subpackage("vte-gtk3-devel")
def _gtk3_devel(self):
    self.pkgdesc = "Gtk+3 terminal widget (development files)"
    return [
        "usr/include/vte-2.91/vte",
        "usr/lib/libvte-2.91.so",
        "usr/lib/pkgconfig/vte-2.91.pc",
        "usr/share/gir-1.0/Vte-2.91.gir",
        "usr/share/vala/vapi/vte-2.91.*",
    ]


@subpackage("vte-gtk4-devel")
def _devel(self):
    self.pkgdesc = "Gtk4 terminal widget (development files)"
    return [
        "usr/include/vte-2.91-gtk4/vte",
        "usr/lib/libvte-2.91-gtk4.so",
        "usr/lib/pkgconfig/vte-2.91-gtk4.pc",
        "usr/share/gir-1.0/Vte-3.91.gir",
        "usr/share/vala/vapi/vte-2.91-gtk4.*",
    ]
