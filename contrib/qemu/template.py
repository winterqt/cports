pkgname = "qemu"
pkgver = "8.0.2"
pkgrel = 0
build_style = "gnu_configure"
# TODO vde liburing libssh capstone
configure_args = [
    "--enable-cap-ng",
    "--enable-curl",
    "--enable-curses",
    "--enable-dbus-display",
    "--enable-docs",
    "--enable-guest-agent",
    "--enable-jack",
    "--enable-gtk",
    "--enable-kvm",
    "--enable-libnfs",
    "--enable-linux-aio",
    "--enable-lzo",
    "--enable-numa",
    "--enable-pie",
    "--enable-sdl",
    "--enable-seccomp",
    "--enable-snappy",
    "--enable-spice",
    "--enable-system",
    "--enable-vhost-net",
    "--enable-virtfs",
    "--enable-tpm",
    "--enable-usb-redir",
    "--enable-virglrenderer",
    "--enable-vnc",
    "--enable-vnc-jpeg",
    "--enable-zstd",
    "--disable-linux-user",
    "--disable-glusterfs",
    "--disable-debug-info",
    "--disable-bsd-user",
    "--disable-werror",
    "--disable-xen",
    "--audio-drv-list=pa,jack,sdl",
]
make_cmd = "gmake"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
    "gmake",
    "bash",
    "perl",
    "flex",
    "bison",
    "bzip2",
    "gettext-tiny",
    "python-sphinx",
    "python-sphinx_rtd_theme",
]
makedepends = [
    "glib-devel",
    "libbz2-devel",
    "zlib-devel",
    "libzstd-devel",
    "lzo-devel",
    "libcap-ng-devel",
    "nss-devel",
    "gnutls-devel",
    "libaio-devel",
    "libjpeg-turbo-devel",
    "pixman-devel",
    "libcurl-devel",
    "dtc-devel",
    "snappy-devel",
    "gtk+3-devel",
    "vte-gtk3-devel",
    "sdl-devel",
    "sdl_image-devel",
    "libpulse-devel",
    "jack-devel",
    "fuse-devel",
    "libseccomp-devel",
    "ncurses-devel",
    "usbredir-devel",
    "pcsc-lite-devel",
    "libcacard-devel",
    "libiscsi-devel",
    "linux-pam-devel",
    "libnuma-devel",
    "libslirp-devel",
    "virglrenderer-devel",
    "libusb-devel",
    "libnfs-devel",
    "spice-devel",
    "spice-protocol",
    "linux-headers",
]
pkgdesc = "Generic machine emulator and virtualizer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://qemu.org"
source = f"https://download.qemu.org/qemu-{pkgver}.tar.xz"
sha256 = "f060abd435fbe6794125e2c398568ffc3cfa540042596907a8b18edca34cf6a5"
suid_files = ["usr/libexec/qemu-bridge-helper"]
file_modes = {
    "etc/qemu/bridge.conf": ("root", "_qemu", 0o640),
    "usr/libexec/qemu-bridge-helper": ("root", "_qemu", 0o4710),
}
# maybe someday
options = ["!cross", "!check"]

system_users = [
    {
        "name": "_qemu",
        "id": None,
        "groups": ["kvm"],
    }
]


def post_install(self):
    self.install_service(self.files_path / "qemu-ga")

    self.install_file(self.files_path / "80-kvm.rules", "usr/lib/udev/rules.d")
    self.install_file(self.files_path / "bridge.conf", "etc/qemu")

    # no elf files in /usr/share
    self.mv(self.destdir / "usr/share/qemu", self.destdir / "usr/lib/qemu")
    self.install_link("../lib/qemu", "usr/share/qemu")

    self.rm(self.destdir / "usr/share/doc", recursive=True)


@subpackage("qemu-guest-agent")
def _guest_agent(self):
    self.pkgdesc = "QEMU guest agent"
    self.depends = []

    return [
        "etc/dinit.d/qemu-ga",
        "usr/bin/qemu-ga",
    ]


@subpackage("qemu-img")
def _img(self):
    self.pkgdesc = "QEMU command line tools for manipulating disk images"
    self.depends = []

    return [
        "usr/bin/qemu-img",
        "usr/bin/qemu-io",
        "usr/bin/qemu-nbd",
        "usr/bin/qemu-storage-daemon",
    ]


@subpackage("qemu-tools")
def _tools(self):
    self.pkgdesc = "QEMU support tools"
    self.depends = []

    return [
        "usr/bin/qemu-edid",
        "usr/bin/qemu-keymap",
        "usr/bin/elf2dmp",
    ]


@subpackage("qemu-pr-helper")
def _pr_helper(self):
    self.pkgdesc = "QEMU pr helper utility"
    self.depends = []

    return [
        "usr/bin/qemu-pr-helper",
        "usr/share/man/man8/qemu-pr-helper.8",
    ]


@subpackage("qemu-vhost-user-gpu")
def _vhost_user_gpu(self):
    self.pkgdesc = "QEMU vhost user GPU device"
    self.depends = []

    return [
        "usr/libexec/vhost-user-gpu",
        "usr/lib/qemu/vhost-user/50-qemu-gpu.json",
    ]


def _spkg(sname):
    @subpackage(f"qemu-system-{sname}")
    def _system(self):
        self.pkgdesc = f"{pkgname} (system-{sname})"
        self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
        self.options = ["foreignelf"]

        extras = []

        match sname:
            case "aarch64":
                extras = [
                    "usr/lib/qemu/edk2-aarch64-code.fd",
                    "usr/lib/qemu/firmware/60-edk2-aarch64.json",
                ]
            case "alpha":
                extras = ["usr/lib/qemu/palcode-clipper"]
            case "arm":
                extras = [
                    "usr/lib/qemu/edk2-arm-code.fd",
                    "usr/lib/qemu/edk2-arm-vars.fd",
                    "usr/lib/qemu/npcm7xx_bootrom.bin",
                    "usr/lib/qemu/firmware/60-edk2-arm.json",
                ]
            case "hppa":
                extras = [
                    "usr/lib/qemu/hppa-firmware.img",
                ]
                self.options += ["execstack"]
            case "i386":
                extras = [
                    "usr/lib/qemu/edk2-i386-code.fd",
                    "usr/lib/qemu/edk2-i386-secure-code.fd",
                    "usr/lib/qemu/edk2-i386-vars.fd",
                    "usr/lib/qemu/firmware/50-edk2-i386-secure.json",
                    "usr/lib/qemu/firmware/60-edk2-i386.json",
                ]
            case "ppc":
                extras = [
                    "usr/lib/qemu/openbios-ppc",
                    "usr/lib/qemu/u-boot.e500",
                    "usr/lib/qemu/u-boot-sam460-20100605.bin",
                ]
                self.options += ["execstack"]
            case "riscv32":
                extras = [
                    "usr/lib/qemu/opensbi-riscv32-generic-fw_dynamic.bin",
                ]
            case "riscv64":
                extras = [
                    "usr/lib/qemu/opensbi-riscv64-generic-fw_dynamic.bin",
                ]
            case "s390x":
                extras = [
                    "usr/lib/qemu/s390-ccw.img",
                    "usr/lib/qemu/s390-netboot.img",
                ]
                self.options += ["execstack"]
            case "sparc":
                extras = [
                    "usr/lib/qemu/openbios-sparc32",
                ]
                self.options += ["execstack"]
            case "sparc64":
                extras = [
                    "usr/lib/qemu/openbios-sparc64",
                ]
                self.options += ["execstack"]
            case "x86_64":
                extras = [
                    "usr/lib/qemu/edk2-x86_64-code.fd",
                    "usr/lib/qemu/edk2-x86_64-secure-code.fd",
                    "usr/lib/qemu/firmware/50-edk2-x86_64-secure.json",
                    "usr/lib/qemu/firmware/60-edk2-x86_64.json",
                ]

        # never strip them
        self.nostrip_files = extras

        return [f"usr/bin/qemu-system-{sname}"] + extras


for _sys in [
    "aarch64",
    "alpha",
    "arm",
    "avr",
    "cris",
    "hppa",
    "i386",
    "loongarch64",
    "m68k",
    "microblaze",
    "microblazeel",
    "mips",
    "mips64",
    "mips64el",
    "mipsel",
    "nios2",
    "or1k",
    "ppc",
    "ppc64",
    "riscv32",
    "riscv64",
    "rx",
    "s390x",
    "sh4",
    "sh4eb",
    "sparc",
    "sparc64",
    "tricore",
    "x86_64",
    "xtensa",
    "xtensaeb",
]:
    _spkg(_sys)

configure_gen = []
