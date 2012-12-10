Name:		calibre
Version:	0.9.8
Release:	2
Summary:	E-book converter and library management
Group:		Office
License:	GPLv3
URL:		http://calibre-ebook.com/
Source0:	http://calibre-ebook.googlecode.com/files/%{name}-%{version}.tar.xz
Source2:	calibre-mount-helper
Patch1:		%{name}-no-update-0.8.6.patch
Patch3:		%{name}-0.7.27-python-fix.patch
Patch4:		%{name}-python2-env-fix.patch
Patch5:		%{name}-web-control.patch
BuildRequires:	python >= 2.6
BuildRequires:	pkgconfig(python) >= 2.6
BuildRequires:	imagemagick-devel
BuildRequires:	python-setuptools
BuildRequires:	qt4-devel 
BuildRequires:	python-qt4-devel
BuildRequires:	pkgconfig(poppler-qt4) >= 0.12
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	podofo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python-mechanize
BuildRequires:	python-lxml
BuildRequires:	python-dateutil
BuildRequires:	python-imaging
BuildRequires:	xdg-utils
BuildRequires:	python-beautifulsoup
BuildRequires:	chmlib-devel
BuildRequires:	python-cssutils >= 0.9.9
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	unzip
BuildRequires:	libwmf-devel
BuildRequires:	libmtp-devel
Requires:	python-qt4
Requires:	python-pypdf
Requires:	python-cherrypy
Requires:	python-cssutils
Requires:	imagemagick
Requires:	python-odf
Requires:	python-django-tagging
Requires:	python-lxml
Requires:	python-imaging
Requires:	python-mechanize
Requires:	python-dateutil
Requires:	python-genshi
Requires:	python-beautifulsoup
Requires:	python-netifaces
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
#-f %{name}.lang
%doc COPYRIGHT LICENSE Changelog.yaml
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
%{_bindir}/ebook-meta
%{_bindir}/ebook-viewer
%{_bindir}/epub-fix
%{_bindir}/fetch-ebook-metadata
%{_bindir}/lrf2lrs
%{_bindir}/lrfviewer
%{_bindir}/lrs2lrf
%{_bindir}/markdown-calibre
%{_bindir}/web2disk
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{python_sitelib}/init_calibre.py*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

# remove redundant / non-free fonts
rm -rf resources/fonts/*/

# don't check for new upstream version (that's what packagers do)
# otherwise the plugins are safe to be updated in ~/.config/calibre/plugins/
%patch1 -F 2 -p1 -b .no-update

# libs
%patch3 -p1 -b .python-fix

# there is no python2 symlink to python2.7
# but just python, as opposed to python3
%patch4 -p1 -b .python2-env-fix

# import from QtNetwork, not Qt
%patch5 -p1 -b .python-web-control

# dos2unix newline conversion
sed -i -e 's/\r//' src/calibre/web/feeds/recipes/*

# fix the location of liberation default font
# sed -i -e "s:P('fonts/liberation/LiberationSerif:('%{_datadir}/fonts/TTF/liberation/LiberationSerif:" \
#  src/calibre/library/catalog.py
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

chmod -x src/calibre/*/*/*/*.py
chmod -x src/calibre/*/*/*.py
chmod -x src/calibre/*/*.py
chmod -x src/calibre/*.py
chmod -x recipes/*.recipe

%build
OVERRIDE_CFLAGS="%{optflags}" python setup.py build 

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
python setup.py install --root=%{buildroot}%{_prefix} \
			--prefix=%{_prefix} \
			--libdir=%{_libdir} \
			--staging-libdir=%{buildroot}%{_libdir} \
# remove shebang from init_calibre.py here because
# it just got spawned by the install script
sed -i -e '/^#!\//, 1d' %{buildroot}%{python_sitelib}/init_calibre.py

# icons
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p resources/images/library.png		  \
   %{buildroot}%{_datadir}/pixmaps/%{name}-gui.png
cp -p resources/images/viewer.png		  \
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

# don't put bash completions in /usr/etc
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{_prefix}%{_sysconfdir}/bash_completion.d/%{name} %{buildroot}%{_sysconfdir}/bash_completion.d
rmdir %{buildroot}%{_prefix}%{_sysconfdir}/bash_completion.d

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

cp -a %{SOURCE2} %{buildroot}%{_bindir}/
