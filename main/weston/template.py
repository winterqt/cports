pkgname = "weston"
pkgver = "12.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=false",
    "-Dlauncher-libseat=true",
    "-Dpipewire=true",
    "-Dremoting=false",
    "-Dbackend-rdp=false",
    "-Dbackend-vnc=false",
    "-Dbackend-drm-screencast-vaapi=true",
    "-Dcolor-management-lcms=true",
    "-Dtest-junit-xml=false",
    "-Db_ndebug=false",
    "-Ddefault_library=shared",
]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = ["meson", "pkgconf", "wayland-progs", "wayland-protocols"]
makedepends = [
    "libpng-devel",
    "libwebp-devel",
    "lcms2-devel",
    "pixman-devel",
    "mesa-devel",
    "pango-devel",
    "cairo-devel",
    "mtdev-devel",
    "glu-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxcursor-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
    "libdrm-devel",
    "linux-pam-devel",
    "udev-devel",
    "dbus-devel",
    "libva-devel",
    "pipewire-devel",
    "libseat-devel",
]
checkdepends = ["mesa-dri", "xwayland"]
pkgdesc = "Reference implementation of a Wayland compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"https://gitlab.freedesktop.org/wayland/{pkgname}/-/releases/{pkgver}/downloads/{pkgname}-{pkgver}.tar.xz"
sha256 = "b18591eab278bc191720f6c09158040b795e7118af1d5ddca6acd9a8e2039535"


def post_install(self):
    self.install_license("COPYING")


@subpackage("weston-x11")
def _x11(self):
    self.depends = [f"weston={pkgver}-r{pkgrel}"]
    self.pkgdesc = f"{pkgdesc} (X11 backend)"

    return ["usr/lib/libweston*/x11-backend.so"]


@subpackage("weston-xwayland")
def _xwayland(self):
    self.depends = [f"weston={pkgver}-r{pkgrel}"]
    self.pkgdecs = f"{pkgdesc} (XWayland plugin)"

    return ["usr/lib/libweston*/xwayland.so"]


@subpackage("weston-libs")
def _lib(self):
    return self.default_libs(extra=[f"usr/lib/libweston-{pkgver[0:2]}"])


@subpackage("weston-devel")
def _devel(self):
    return self.default_devel()
