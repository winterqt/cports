pkgname = "libreoffice"
pkgver = "7.5.4.2"
pkgrel = 1
# riscv64: no handling of libcxxabi + likely too slow
archs = ["x86_64", "ppc64le", "aarch64"]
build_style = "gnu_configure"
configure_args = [
    "--with-vendor=Chimera Linux",
    "--with-help",
    "--disable-fetch-external",
    "--disable-odk",
    "--disable-online-update",
    "--disable-dependency-tracking",
    "--disable-qt5",
    "--disable-kf5",
    "--disable-gtk3-kde5",
    "--disable-dconf",
    "--disable-epm",
    "--disable-ldap",
    "--disable-lpsolve",
    "--disable-coinmp",
    "--disable-firebird-sdbc",
    "--disable-mariadb-sdbc",
    "--disable-postgresql-sdbc",
    "--enable-release-build",
    "--enable-split-app-modules",
    "--enable-python=system",
    "--enable-introspection",
    "--enable-gtk3",
    "--enable-gtk4",
    "--enable-qt6",
    "--enable-build-opensymbol",
    "--with-external-dict-dir=/usr/share/hunspell",
    "--with-external-hyph-dir=/usr/share/hyphen",
    "--with-system-libs",
    "--with-system-headers",
    "--with-tls=nss",
    "--with-myspell-dicts",
    "--without-java",
    "--without-fonts",
    "--without-system-box2d",
    "--without-system-libcmis",
    "--without-system-libzmf",
    "--without-system-libstaroffice",
    "--without-system-dragonbox",
    "--without-system-libfixmath",
]
configure_env = {"NOCONFIGURE": "1", "QT6DIR": "/usr/lib/qt6"}
configure_gen = ["perl", "autogen.sh"]
make_cmd = "gmake"
make_dir = "."
make_build_target = "build"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
    "automake",
    "libtool",
    "bash",
    "flex",
    "bison",
    "gperf",
    "hyphen",
    "icu",
    "gettext-tiny",
    "gnupg",
    "xz",
    "zip",
    "unzip",
    "xsltproc",
    "libxml2-progs",
    "sane-backends",
    "fontforge-cli",
    "python-setuptools",
    "python-lxml",
    "qt6-qtbase",
    "gtk4-devel",
    "gobject-introspection",
]
makedepends = [
    "abseil-cpp-devel",
    "avahi-devel",
    "bluez-devel",
    "boost-devel",
    "cairo-devel",
    "clucene-devel",
    "cppunit-devel",
    "fontconfig-devel",
    "freetype-devel",
    "glm",
    "gpgme-devel",
    "graphite2-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "harfbuzz-devel",
    "hunspell-devel",
    "hyphen-devel",
    "icu-devel",
    "lcms2-devel",
    "libabw-devel",
    "libatomic_ops-devel",
    "libcdr-devel",
    "libcurl-devel",
    "libe-book-devel",
    "libepoxy-devel",
    "libepubgen-devel",
    "libetonyek-devel",
    "libexpat-devel",
    "libexttextcat-devel",
    "libfreehand-devel",
    "libgcrypt-devel",
    "libgirepository-devel",
    "libjpeg-turbo-devel",
    "libltdl-devel",
    "libmspub-devel",
    "libmwaw-devel",
    "libnumbertext-devel",
    "libodfgen-devel",
    "liborcus-devel",
    "libpagemaker-devel",
    "libpng-devel",
    "libpoppler-cpp-devel",
    "libqxp-devel",
    "librevenge-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libtommath-devel",
    "libvisio-devel",
    "libwebp-devel",
    "libwpg-devel",
    "libwps-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libxt-devel",
    "mdds",
    "mythes-devel",
    "neon-devel",
    "nss-devel",
    "nspr-devel",
    "openjpeg-devel",
    "openssl-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "redland-devel",
    "sane-backends-devel",
    "unixodbc-devel",
    "xmlsec1-devel",
    "zlib-devel",
    "zxing-cpp-devel",
]
pkgdesc = "Free office suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.libreoffice.org"
# big and not particularly useful testsuite
options = ["!cross", "!check"]

_surl = f"https://download.documentfoundation.org/libreoffice/src/{pkgver[:-2]}"
_aurl = "https://dev-www.libreoffice.org/src"
_eurl = "https://dev-www.libreoffice.org/extern"

source = [
    (f"{_surl}/{pkgname}-{pkgver}.tar.xz", True),
    (f"{_surl}/{pkgname}-dictionaries-{pkgver}.tar.xz", True),
    (f"{_surl}/{pkgname}-help-{pkgver}.tar.xz", True),
    (f"{_surl}/{pkgname}-translations-{pkgver}.tar.xz", True),
    (f"{_aurl}/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip", False),
    (f"{_aurl}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip", False),
    (f"{_aurl}/ace6ab49184e329db254e454a010f56d-libxml-1.1.7.zip", False),
    (f"{_aurl}/language-subtag-registry-2022-08-08.tar.bz2", False),
    (f"{_aurl}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip", False),
    (f"{_aurl}/d8bd5eed178db6e2b18eeed243f85aa8-flute-1.1.6.zip", False),
    (f"{_aurl}/ba2930200c9f019c2d93a8c88c651a0f-flow-engine-0.9.4.zip", False),
    (f"{_aurl}/box2d-2.4.1.tar.gz", False),
    (f"{_aurl}/libcmis-0.5.2.tar.xz", False),
    (f"{_aurl}/libstaroffice-0.0.7.tar.xz", False),
    (f"{_aurl}/libzmf-0.0.2.tar.xz", False),
    (f"{_aurl}/pdfium-5408.tar.bz2", False),
    (
        f"{_eurl}/8249374c274932a21846fa7629c2aa9b-officeotron-0.7.4-master.jar",
        False,
    ),
    (
        f"{_eurl}/odfvalidator-0.9.0-RC2-SNAPSHOT-jar-with-dependencies-2726ab578664434a545f8379a01a9faffac0ae73.jar",
        False,
    ),
    (f"{_aurl}/dtoa-20180411.tgz", False),
    (f"{_aurl}/beeca87be45ec87d241ddd0e1bad80c1-bsh-2.0b6-src.zip", False),
    (f"{_aurl}/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip", False),
    (f"{_aurl}/b7cae45ad2c23551fd6ccb8ae2c1f59e-numbertext_0.9.5.oxt", False),
    (f"{_aurl}/eeb2c7ddf0d302fba4bfc6e97eac9624-libbase-1.1.6.zip", False),
    (f"{_aurl}/3bdf40c0d199af31923e900d082ca2dd-libfonts-1.1.6.zip", False),
    (f"{_aurl}/3404ab6b1792ae5f16bbd603bd1e1d03-libformula-1.1.7.zip", False),
    (f"{_aurl}/db60e4fde8dd6d6807523deb71ee34dc-liblayout-0.2.10.zip", False),
    (f"{_aurl}/97b2d4dba862397f446b217e2b623e71-libloader-1.1.6.zip", False),
    (
        f"{_aurl}/8ce2fcd72becf06c41f7201d15373ed9-librepository-1.1.6.zip",
        False,
    ),
    (
        f"{_aurl}/f94d9870737518e3b597f9265f4e9803-libserializer-1.1.6.zip",
        False,
    ),
    (f"{_aurl}/39bb3fcea1514f1369fcfc87542390fd-sacjava-1.3.zip", False),
    (
        f"{_aurl}/skia-m103-b301ff025004c9cd82816c86c547588e6c24b466.tar.xz",
        False,
    ),
    (f"{_aurl}/dragonbox-1.1.3.tar.gz", False),
]
sha256 = [
    "68bbd1b79ffa4c33ed80f25520b9e6d69e3be23c9b4a0f0c9d859cc9a24865e8",
    "4f2dbe571e2116ce11df71d72b4ae03f7a3ca82c72578c1724afb3bd26d38d08",
    "a90f931dd3238eb64e6f65964ea8f90e5accd9ad10925d5a60c7af6aa585c1f1",
    "7eb264c2cd66f028831535bec0d3fcdfb687fae4deb77d200cfe4034ca3a10ad",
    "1fb458d6aab06932693cc8a9b6e4e70944ee1ff052fa63606e3131df34e21753",
    "75823776fb51a9c526af904f1503a7afaaab900fba83eda64f8a41073724c870",
    "7d2797fe9f79a77009721e3f14fa4a1dec17a6d706bdc93f85f1f01d124fab66",
    "e2d9224e0e50fc8ad12a3cf47396bbcadf45b2515839d4770432653a88972c00",
    "d30b13f4ba2e3b6a2d4f020c0dee0a9fb9fc6fbcc2d561f36b78da4bf3802370",
    "1b5b24f7bc543c0362b667692f78db8bab4ed6dafc6172f104d0bd3757d8a133",
    "233f66e8d25c5dd971716d4200203a612a407649686ef3b52075d04b4c9df0dd",
    "d6b4650ff897ee1ead27cf77a5933ea197cbeef6705638dd181adc2e816b23c2",
    "d7b18d9602190e10d437f8a964a32e983afd57e2db316a07d87477a79f5000a2",
    "f94fb0ad8216f97127bedef163a45886b43c62deac5e5b0f5e628e234220c8db",
    "27051a30cb057fdb5d5de65a1f165c7153dc76e27fe62251cbb86639eb2caf22",
    "7db59b1e91f2bc0ab4c5e19d1a4f881e6a47dbb0d3b7e980a7358225b12a0f35",
    "f2443f27561af52324eee03a1892d9f569adc8db9e7bca55614898bc2a13a770",
    "d55495ab3a86544650587de2a72180ddf8bfc6376d14ddfa923992dbc86a06e0",
    "0082d0684f7db6f62361b76c4b7faba19e0c7ce5cb8e36c4b65fea8281e711b4",
    "9e93c73e23aff644b17dfff656444474c14150e7f3b38b19635e622235e01c96",
    "64585ac36a81291a58269ec5347e7e3e2e8596dbacb9221015c208191333c6e1",
    "1568ed1d2feb8210bb5de61d69574a165cded536cfa17c6953c9064076469de2",
    "75c80359c9ce343c20aab8a36a45cb3b9ee7c61cf92c13ae45399d854423a9ba",
    "e0531091787c0f16c83965fdcbc49162c059d7f0c64669e7f119699321549743",
    "5826d1551bf599b85742545f6e01a0079b93c1b2c8434bf409eddb3a29e4726b",
    "e1fb87f3f7b980d33414473279615c4644027e013012d156efa538bc2b031772",
    "3d853b19b1d94a6efa69e7af90f7f2b09ecf302913bee3da796c15ecfebcfac8",
    "abe2c57ac12ba45d83563b02e240fa95d973376de2f720aab8fe11f2e621c095",
    "05640a1f6805b2b2d7e2cb9c50db9a5cb084e3c52ab1a71ce015239b4a1d4343",
    "085f2112c51fa8c1783fac12fbd452650596415121348393bb51f0f7e85a9045",
    "c094a6247e44104beaaa0d00c825beb6baf1a8e532dc22214747495317a65bd9",
    "09d63b05e9c594ec423778ab59b7a5aa1d76fdd71d25c7048b0258c4ec9c3384",
]

tool_flags = {
    "CXXFLAGS": ["-DGLM_ENABLE_EXPERIMENTAL", "-DU_USING_ICU_NAMESPACE=1"]
}


_langs = []


def post_extract(self):
    from cbuild.core import paths

    srcp = paths.sources() / f"{pkgname}-{pkgver}"

    # copy the files over
    for s, ext in source[1:]:
        self.cp(srcp / s[s.rfind("/") + 1 :], self.cwd)

    # copy over patches
    self.cp(self.files_path / "skia-no-execinfo.patch.1", "external/skia")


def init_configure(self):
    if self.profile().endian == "big":
        self.configure_args += ["--disable-skia"]
    if self.has_lto():
        self.configure_args += ["--enable-lto"]
    self.configure_args += [
        "--with-parallelism=" + str(self.conf_jobs),
        "--with-lang=" + " ".join(_langs),
        "--with-external-tar=" + str(self.chroot_cwd),
    ]


def post_build(self):
    self.make.invoke(["-C", "libreofficekit"])


def do_install(self):
    self.make.invoke(
        [
            f"DESTDIR={self.chroot_destdir / 'all'}",
            "PREFIXDIR=/usr",
            "distro-pack-install",
        ]
    )
    # move stuff out
    self.mv(self.destdir / "all/usr", self.destdir)
    # qt6 is not installed for some reason?
    self.install_file(
        "instdir/program/libvclplug_qt6lo.so",
        "usr/lib/libreoffice/program",
        mode=0o755,
    )


def _take_list(self, listn):
    lcwd = self.parent.cwd
    with open(lcwd / f"file-lists/{listn}_list.txt") as fl:
        for f in fl:
            if f.startswith("%"):
                continue
            self.take(f.strip().removeprefix("/"))
    # also take appdata file if there is one
    self.take(
        f"usr/share/metainfo/libreoffice-{listn}.appdata.xml", missing_ok=True
    )


def _add_lang(langc, langd, langs):
    _langs.append(langc.replace("_", "-"))

    @subpackage(f"{pkgname}-lang_{langc.lower()}")
    def _lang(self):
        self.pkgdesc = f"{pkgdesc} ({langd} language pack)"

        # soft-install at least one langpack by default
        if langc == "en_US":
            self.install_if = [f"{pkgname}-common={pkgver}-r{pkgrel}"]

        def inst():
            _take_list(self, f"lang_{langc}")

        return inst


for _langc, _langd in [
    ("af", "Afrikaans"),
    ("am", "Amharic"),
    ("ar", "Arabic"),
    ("as", "Assamese"),
    ("ast", "Asturian"),
    ("be", "Belarusian"),
    ("bg", "Bulgarian"),
    ("bn", "Bengali"),
    ("bn_IN", "Bengali (India)"),
    ("bo", "Tibetan"),
    ("br", "Breton"),
    ("brx", "Bodo"),
    ("bs", "Bosnian"),
    ("ca", "CatCalan"),
    ("ca_valencia", "Catalan (Valencian)"),
    ("ckb", "Central Kurdish"),
    ("cs", "Czech"),
    ("cy", "Welsh (Cymraeg)"),
    ("da", "Danish"),
    ("de", "German"),
    ("dgo", "Dogri proper"),
    ("dsb", "Lower Sorbian"),
    ("dz", "Dzongkha"),
    ("el", "Greek"),
    ("en_GB", "English (UK)"),
    ("en_US", "English (US)"),
    ("en_ZA", "English (South Africa)"),
    ("eo", "Esperanto"),
    ("es", "Spanish"),
    ("et", "Estonian"),
    ("eu", "Basque"),
    ("fa", "Persian (Farsi)"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("fur", "Friulian"),
    ("fy", "Frisian"),
    ("ga", "Irish"),
    ("gd", "Scottish Gaelic"),
    ("gl", "Galician"),
    ("gu", "Gujarati"),
    ("gug", "Guaraní (Paraguay)"),
    ("he", "Hebrew"),
    ("hi", "Hindi"),
    ("hr", "Croatian"),
    ("hsb", "Upper Sorbian"),
    ("hu", "Hungarian"),
    ("id", "Indonesian"),
    ("is", "Icelandic"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ka", "Georgian"),
    ("kab", "Kabyle"),
    ("kk", "Kazakh"),
    ("km", "Khmer"),
    ("kmr_Latn", "Kurmanji Kurdish (Latin)"),
    ("kn", "Kannada"),
    ("ko", "Korean"),
    ("kok", "Konkani"),
    ("ks", "Kashmiri"),
    ("lb", "Luxembourgish"),
    ("lo", "Lao"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("mai", "Maithili"),
    ("mk", "Macedonian"),
    ("ml", "Malayalam"),
    ("mn", "Mongolian"),
    ("mni", "Meithei (Manipuri)"),
    ("mr", "Marathi"),
    ("my", "Burmese"),
    ("nb", "Norwegian (Bokmal)"),
    ("ne", "Nepali"),
    ("nl", "Dutch"),
    ("nn", "Nynorsk"),
    ("nr", "Ndebele (South)"),
    ("nso", "Northern Sotho"),
    ("oc", "Occitan"),
    ("om", "Oromo"),
    ("or", "Oriya"),
    ("pa_IN", "Punjabi (India)"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("pt_BR", "Portuguese (Brazil)"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("rw", "Kinyarwanda"),
    ("sa_IN", "Sanskrit (India)"),
    ("sat", "Santali"),
    ("sd", "Sindhi"),
    ("si", "Sinhala"),
    ("sid", "Sidamo"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("sq", "Albanian"),
    ("sr", "Serbian"),
    ("sr_Latn", "Serbian (Latin)"),
    ("ss", "Swati"),
    ("st", "Southern, Sotho"),
    ("sv", "Swedish"),
    ("sw_TZ", "Swahili (Tanzania)"),
    ("szl", "Silesian"),
    ("ta", "Tamil"),
    ("te", "Telugu"),
    ("tg", "Tajik"),
    ("th", "Thai"),
    ("tn", "Tswana"),
    ("tr", "Turkish"),
    ("ts", "Tsonga"),
    ("tt", "Tatar"),
    ("ug", "Uyghur"),
    ("uk", "Ukrainian"),
    ("uz", "Uzbek"),
    ("ve", "Venda"),
    ("vec", "Venetian"),
    ("vi", "Vietnamese"),
    ("xh", "Xhosa"),
    ("zh_CN", "Simplified Chinese (People's Republic of China)"),
    ("zh_TW", "Traditional Chinese (Taiwan)"),
    ("zu", "Zulu"),
]:
    _add_lang(_langc, _langd, _langs)


def _gensub(subn, subd):
    @subpackage(f"{pkgname}-{subn}")
    def _sub(self):
        self.pkgdesc = f"{pkgdesc} ({subd})"
        if subn == "writer" or subn == "gnome":
            self.depends = [f"{pkgname}-common={pkgver}-r{pkgrel}"]
        else:
            # the other apps can't launch without writer being present
            self.depends = [f"{pkgname}-writer={pkgver}-r{pkgrel}"]

        # we install gtk integration always by default, to give people
        # a decent UI out of box, but make it a softdep (removable)
        # other stuff is soft-installed by the full metapackage
        if subn == "gnome":
            self.install_if = [f"{pkgname}-common={pkgver}-r{pkgrel}"]
        else:
            self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

        def inst():
            _take_list(self, subn)

        return inst


for _subn, _subd in [
    ("base", "database"),
    ("calc", "spreadsheet"),
    ("draw", "graphics"),
    ("gnome", "GTK integration"),
    ("impress", "presentations"),
    ("math", "equation editor"),
    ("writer", "word processor"),
]:
    _gensub(_subn, _subd)


@subpackage(f"{pkgname}-qt6")
def _qt6(self):
    self.pkgdesc = f"{pkgdesc} (Qt6 integration)"
    self.depends = [f"{pkgname}-common={pkgver}-r{pkgrel}"]
    # qt6 integration for those who already have qt
    self.install_if = [f"{pkgname}-common={pkgver}-r{pkgrel}", "qt6-qtbase-gui"]

    return ["usr/lib/libreoffice/program/libvclplug_qt6lo.so"]


@subpackage(f"{pkgname}-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"

    # we don't use the list, just take all remaining files at the end
    return ["usr"]
