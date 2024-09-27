%define _disable_ld_no_undefined 1
%define _disable_lto 1

Name:		calibre
Version:	7.19.0
%define MathJax_version 3.2.2
Release:	1
Summary:	E-book converter and library management
Group:		Office
License:	GPLv3
URL:		https://calibre-ebook.com/
Source0:	http://code.calibre-ebook.com/dist/src/%{name}-%{version}.tar.xz
Source1:	https://github.com/LibreOffice/dictionaries/archive/master/hyphenation-dictionaries.tar.gz
# (mandian) FIXME: use this until version 3.x is packaged
Source2:	https://github.com/mathjax/MathJax/archive/%{MathJax_version}/MathJax-%{MathJax_version}.tar.gz
Source3:	https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/main/iso-codes-main.zip
Source4:	calibre-mount-helper
# (tpg) looks like this is missing
Source5:	user-agent-data.json
Source100:	calibre.rpmlintrc
Patch1:		calibre-2.9.0-fdo-no_update.patch
Patch2:		calibre-5.9.0-compile.patch
Patch3:		calibre-6.12.0-python-fix.patch
Patch4:		calibre-6.12.0-nousrlib.patch
Patch5:		calibre-6.12.0-compile.patch
Patch6:		calibre-7.19.0-fix-build-with-predownloaded-isocodes.patch

BuildRequires:	pkgconfig(python3)
BuildRequires:	imagemagick-devel
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	mathjax
BuildRequires:	qmake-qt6
BuildRequires:	qt6-cmake
BuildRequires:	hyphen-devel
BuildRequires:	python-qt6
BuildRequires:	python-qt6-devel
BuildRequires:	python-sip
BuildRequires:	python-sphinx
BuildRequires:	python-sip-qt6
BuildRequires:	python-qt6-webengine
BuildRequires:	python-qt-builder >= 1.7.0
BuildRequires:	fonts-ttf-liberation
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(poppler-qt6) >= 0.12
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(uchardet)
BuildRequires:	podofo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python%{pyver}dist(mechanize)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(css-parser)
BuildRequires:	python%{pyver}dist(feedparser)
BuildRequires:	python%{pyver}dist(netifaces)
BuildRequires:	python%{pyver}dist(beautifulsoup4)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(soupsieve)
BuildRequires:	python%{pyver}dist(msgpack)
BuildRequires:	python%{pyver}dist(regex)
BuildRequires:	python%{pyver}dist(html5-parser) >= 0.4.8
BuildRequires:	python%{pyver}dist(xxhash)
BuildRequires:	python%{pyver}dist(zeroconf)
BuildRequires:	python-html2text
BuildRequires:	bash-completion
#BuildRequires:	python%{pyver}dist(zeroconf)
BuildRequires:	python%{pyver}dist(markdown) 
BuildRequires:	xdg-utils
BuildRequires:	chmlib-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	unzip
BuildRequires:	libwmf-devel
BuildRequires:	libmtp-devel
BuildRequires:	python%{pyver}dist(apsw)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	libstemmer-devel
BuildRequires:	cmake(XKB)
BuildRequires:	pkgconfig(xkbcommon)

Requires:	fonts-ttf-liberation
Requires:	imagemagick
Requires:	mathjax
Requires:	python%{pyver}dist(css-parser)
Requires:	python%{pyver}dist(odfpy)
Requires:	python%{pyver}dist(pillow)
Requires:	python-dbus
Requires:	python%{pyver}dist(apsw)
Requires:	python%{pyver}dist(jeepney)
Requires:	python%{pyver}dist(lxml)
Requires:	python%{pyver}dist(mechanize)
Requires:	python%{pyver}dist(python-dateutil)
Requires:	python%{pyver}dist(beautifulsoup4)
Requires:	python%{pyver}dist(netifaces)
Requires:	python%{pyver}dist(dnspython)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(pygments)
Requires:	python%{pyver}dist(msgpack)
Requires:	python%{pyver}dist(regex)
Requires:	python%{pyver}dist(six)
Requires:	python%{pyver}dist(markdown)
Requires:	python%{pyver}dist(feedparser)
Requires:	python%{pyver}dist(soupsieve)
Requires:	python%{pyver}dist(xxhash)
Requires:	python-sip
Requires:	python-qt6
Requires:	python-qt6-webengine
Requires:	qt6-qtwebengine
Requires:	python-html5-parser
Requires:	python%{pyver}dist(html5-parser)
# FIXME why is this not autodetected?
Requires:	python-zeroconf
Requires:	optipng
Requires:	poppler
# Require the packages of the files which are symlinked by calibre
Requires:	fonts-ttf-liberation
# E-mail functionality requires this package
# see https://bugs.launchpad.net/calibre/+bug/739073
Requires:	python-dnspython

%description
Calibre is meant to be a complete e-library solution. It includes library
management, format conversion, news feeds to ebook conversion as well as
e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical book,
i.e. a single entry in the database that may correspond to ebooks in several
formats. It also supports conversion to and from a dozen different ebook
formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, CHM, ODT, HTML, CBR, CBZ,
RTF, TXT, PDF and LRS.

%files
%doc COPYRIGHT LICENSE
%{_bindir}/calibre
%{_bindir}/calibre-complete
%{_bindir}/calibre-customize
%{_bindir}/calibre-debug
%{_bindir}/calibre-parallel
%{_bindir}/calibre-server
%{_bindir}/calibre-smtp
%{_bindir}/calibre-mount-helper
%{_bindir}/calibredb
%{_bindir}/ebook-convert
%{_bindir}/ebook-device
%{_bindir}/ebook-edit
%{_bindir}/ebook-meta
%{_bindir}/ebook-polish
%{_bindir}/ebook-viewer
%{_bindir}/fetch-ebook-metadata
%{_bindir}/lrf2lrs
%{_bindir}/lrfviewer
%{_bindir}/lrs2lrf
%{_bindir}/markdown-calibre
%{_bindir}/web2disk
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/calibre-mimetypes.xml

%{_datadir}/bash-completion/completions/*
%{_datadir}/metainfo/calibre-ebook-edit.metainfo.xml
%{_datadir}/metainfo/calibre-ebook-viewer.metainfo.xml
%{_datadir}/metainfo/calibre-gui.metainfo.xml

%{python_sitelib}/init_calibre.py*
#{python_sitelib}/__pycache__/init_calibre.*.py*

#--------------------------------------------------------------------

%prep
%autosetup -p1

cp %{S:3} /tmp

# remove redundant / non-free fonts
rm -rf resources/fonts/*/

# dos2unix newline conversion
sed -i -e 's/\r//' src/calibre/web/feeds/recipes/*

# fix the location of liberation default font
# sed -i -e "s:P('fonts/liberation/LiberationSerif:('%{_datadir}/fonts/TTF/liberation/LiberationSerif:" \
#	src/calibre/library/catalog.py
sed -i -e "s:P('fonts/liberation/LiberationSerif:('%{_datadir}/fonts/TTF/liberation/LiberationSerif:" \
	src/calibre/utils/magick/draw.py
sed -i -e "s:P('fonts/liberation/LiberationSerif:('%{_datadir}/fonts/TTF/liberation/LiberationSerif:" \
	src/calibre/web/feeds/news.py
sed -i -e "s:P('fonts/liberation/LiberationSerif:('%{_datadir}/fonts/TTF/liberation/LiberationSerif:" \
	recipes/*_ke.recipe

# remove shebangs
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*.py
sed -i -e '/^#![ ]*\//, 1d' src/calibre/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*.py
sed -i -e '/^#!\//, 1d' src/templite/*.py
sed -i -e '/^#!\//, 1d' resources/default_tweaks.py
sed -i -e '/^#!\//, 1d' recipes/*.recipe

# Remove superfluous bits
rm -rf bypy

chmod -x src/calibre/*/*/*/*.py
chmod -x src/calibre/*/*/*.py
chmod -x src/calibre/*/*.py
chmod -x src/calibre/*.py
chmod -x recipes/*.recipe

cp %{SOURCE5} resources/

%build
tar xf %{S:1}
tar xf %{S:2}
export OVERRIDE_CFLAGS="%{optflags}"
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py build
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py iso_data \
	--path-to-isocodes %{S:3}
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py iso639 \
	--path-to-isocodes %{S:3}
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py iso3166 \
	--path-to-isocodes %{S:3}
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py translations
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py gui
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py resources \
	--path-to-liberation_fonts %{_datadir}/fonts/TTF/liberation \
	--system-liberation_fonts \
	--path-to-hyphenation `pwd`/dictionaries-master \
	--path-to-mathjax `pwd`/MathJax-%{MathJax_version}
#	--system-mathjax \
#	--path-to-mathjax %{_libdir}/javascript/mathjax
PODOFO_LIB_DIR=%{_libdir} CXX=clang++ CC=clang python setup.py man_pages

%install
mkdir -p %{buildroot}%{_datadir}

# create directories for xdg-utils
mkdir -p %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
mkdir -p %{buildroot}%{_datadir}/packages
mkdir -p %{buildroot}%{_datadir}/mime
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/desktop-directories

# create directory for calibre environment module
# the install script assumes it's there.
mkdir -p %{buildroot}%{python_sitelib}

XDG_DATA_DIRS="%{buildroot}%{_datadir}" \
XDG_UTILS_INSTALL_MODE="system" \
LIBPATH="%{_libdir}" \
LANG="en_US.UTF-8" \
python setup.py install --root=%{buildroot}%{_prefix} \
			--prefix=%{_prefix} \
			--libdir=%{_libdir} \
			--staging-libdir=%{buildroot}%{_libdir} \

# remove shebang from init_calibre.py here because
# it just got spawned by the install script
sed -i -e '/^#!\//, 1d' %{buildroot}%{python_sitelib}/init_calibre.py

# icons
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p resources/images/library.png		\
	%{buildroot}%{_datadir}/pixmaps/%{name}-gui.png
cp -p resources/images/viewer.png		\
	%{buildroot}%{_datadir}/pixmaps/calibre-viewer.png

# every file is empty here
find %{buildroot}%{_datadir}/mime -maxdepth 1 -type f|xargs rm -f

# the portable batch (>=0.8.5) is not needed
rm -f %{buildroot}%{_bindir}/calibre-portable.bat

# packages aren't allowed to register mimetypes like this
rm -f %{buildroot}%{_datadir}/applications/defaults.list
rm -f %{buildroot}%{_datadir}/applications/mimeinfo.cache
rm -f %{buildroot}%{_datadir}/mime/application/*.xml
rm -f %{buildroot}%{_datadir}/mime/text/*.xml

# Add desktop files
cat >%{buildroot}%{_datadir}/applications/calibre-ebook-viewer.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=E-book Viewer
GenericName=Viewer for E-books
Comment=Viewer for E-books in all the major formats
TryExec=ebook-viewer
Exec=ebook-viewer --detach %f
Icon=calibre-viewer
Categories=Graphics;Viewer;
MimeType=text/plain;application/x-mobipocket-subscription;application/vnd.openxmlformats-officedocument.wordprocessingml.document;text/html;application/x-cbc;application/ereader;application/oebps-package+xml;image/vnd.djvu;application/x-sony-bbeb;application/vnd.ms-word.document.macroenabled.12;text/rtf;text/x-markdown;application/pdf;application/x-cbz;application/x-cbr;application/x-mobi8-ebook;text/fb2+xml;application/vnd.oasis.opendocument.text;application/epub+zip;application/x-mobipocket-ebook;application/xhtml+xml;
EOF
cat >%{buildroot}%{_datadir}/applications/calibre-gui.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=calibre
GenericName=E-book library management
Comment=E-book library management: Convert, view, share, catalogue all your e-books
TryExec=calibre
Exec=calibre --detach %F
Icon=calibre-gui
Categories=Office;
MimeType=text/plain;application/x-mobipocket-subscription;application/vnd.openxmlformats-officedocument.wordprocessingml.document;text/html;application/x-cbc;application/ereader;application/oebps-package+xml;image/vnd.djvu;application/x-sony-bbeb;application/vnd.ms-word.document.macroenabled.12;text/rtf;text/x-markdown;application/pdf;application/x-cbz;application/x-cbr;application/x-mobi8-ebook;text/fb2+xml;application/vnd.oasis.opendocument.text;application/epub+zip;application/x-mobipocket-ebook;application/xhtml+xml;
EOF
cat >%{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop <<'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=LRF Viewer
GenericName=Viewer for LRF files
Comment=Viewer for LRF files (SONY ebook format files)
TryExec=lrfviewer
Exec=lrfviewer %f
Icon=calibre-viewer
MimeType=application/x-sony-bbeb;
Categories=Graphics;Viewer;
EOF

desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-ebook-viewer.desktop
desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-gui.desktop
desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop

# mimetype icon for lrf
rm -rf %{buildroot}%{_datadir}/icons/hicolor/128x128
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/images/mimetypes/lrf.png \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-sony-bbeb.png
cp -p resources/images/viewer.png \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/calibre-viewer.png

# these are provided as separate packages
rm -rf %{buildroot}%{_libdir}/%{name}/{odf,cherrypy,pyPdf,encutils,cssutils}
rm -rf %{buildroot}%{_libdir}/%{name}/cal/utils/genshi
rm -rf %{buildroot}%{_libdir}/%{name}/cal/trac

# link to system fonts after we have deleted the non-free ones
# http://oldbugs.calibre-ebook.com/ticket/3832
mkdir -p %{buildroot}%{_datadir}/%{name}/fonts/prs500
ln -s %{_datadir}/fonts/TTF/liberation/LiberationSans-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0003m_.ttf
ln -s %{_datadir}/fonts/TTF/liberation/LiberationSerif-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0011m_.ttf
ln -s %{_datadir}/fonts/TTF/liberation/LiberationMono-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0419m_.ttf

# localization has changed since calibre-0.8.5
# locale.zip is treated internally at runtime
# so the traditional locale fixes are moot.
# locales should still be looked for in the proper place
# but under the new localization zip-based schema
sed -i -e 's:localization/locale.zip:%{_datadir}/%{name}/localization/locales.zip:' %{buildroot}%{_libdir}/%{name}/%{name}/utils/localization.py

#% find_lang %{name} --with-kde --all-name

rm -f %{buildroot}%{_bindir}/%{name}-uninstall

install -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/

rm /tmp/$(basename %{S:3})
