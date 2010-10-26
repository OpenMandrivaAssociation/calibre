Name:		calibre
Version:	0.7.24
Release:	%mkrel 1
Summary:	E-book converter and library management
Group:		Text tools 
License:	GPL
URL:		http://calibre-ebook.com/
Source0:	http://calibre-ebook.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-manpages.patch
Patch1:		%{name}-no-update.patch
Patch3:		%{name}-0.6.47-python-fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	python >= 2.6
BuildRequires:	python-devel >= 2.6
BuildRequires:	ImageMagick-devel
BuildRequires:	python-setuptools
BuildRequires:	qt4-devel 
BuildRequires:	python-qt4-devel
BuildRequires:	python-qt4-scripttools
BuildRequires:	libpoppler-qt4-devel >= 0.12
BuildRequires:	podofo-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python-mechanize
BuildRequires:	python-lxml
BuildRequires:	python-cssutils >= 0.9.6
BuildRequires:	python-dateutil
BuildRequires:	python-imaging
BuildRequires:	python-sqlite2
BuildRequires:	xdg-utils
BuildRequires:	python-beautifulsoup
BuildRequires:	unzip
BuildRequires:	libwmf-devel
BuildRequires:	chmlib-devel

Requires:	PyQt4
Requires:	pyPdf
Requires:	python-cherrypy
Requires:	python-cssutils
Requires:	ImageMagick
Requires:	python-odf
Requires:	python-django-tagging
Requires:	python-lxml
Requires:	python-imaging
Requires:	python-mechanize
Requires:	python-dateutil
Requires:	python-genshi
Requires:	python-beautifulsoup

%description
Calibre is meant to be a complete e-library solution. It includes library
management, format conversion, news feeds to ebook conversion as well as
e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical book,
i.e. a single entry in the database that may correspond to ebooks in several
formats. It also supports conversion to and from a dozen different ebook
formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, ODT, HTML, CBR, CBZ, RTF,
TXT, PDF, CHM and LRS.

%prep
%setup -q -n %{name}

# remove redundant / non-free fonts
rm -rf resources/fonts/*

%patch0 -p1 -b .manpages
%patch1 -p1 -b .no-update
%patch3 -p1 -b .python-fix

# dos2unix newline conversion
%{__sed} -i 's/\r//' src/calibre/web/feeds/recipes/*

# remove shebangs
%{__sed} -i -e '/^#!\//, 1d' src/calibre/*/*/*/*.py
%{__sed} -i -e '/^#!\//, 1d' src/calibre/*/*/*.py
%{__sed} -i -e '/^#![ ]*\//, 1d' src/calibre/*/*.py
%{__sed} -i -e '/^#!\//, 1d' src/calibre/*.py
%{__sed} -i -e '/^#!\//, 1d' resources/recipes/*

%{__chmod} -x src/calibre/*/*/*/*.py
%{__chmod} -x src/calibre/*/*/*.py
%{__chmod} -x src/calibre/*/*.py
%{__chmod} -x src/calibre/*.py
%{__chmod} -x resources/recipes/*


%build
OVERRIDE_CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}

# create directories for xdg-utils
mkdir -p %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
mkdir -p %{buildroot}%{_datadir}/packages
mkdir -p %{buildroot}%{_datadir}/mime
mkdir -p %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/desktop-directories
mkdir -p %{buildroot}%{python_sitelib}
XDG_DATA_DIRS="%{buildroot}%{_datadir}" \
XDG_UTILS_INSTALL_MODE="system" \
LIBPATH="%{_libdir}" \
python setup.py install --root=%{buildroot}%{_prefix} \
			--prefix=%{_prefix} \
			--libdir=%{_libdir} \
			--staging-libdir=%{buildroot}%{_libdir}

%{__sed} -i -e '/^#!\//, 1d' %{buildroot}%{python_sitelib}/init_calibre.py
# icons
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p resources/images/library.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}-gui.png
cp -p resources/images/viewer.png \
	%{buildroot}%{_datadir}/pixmaps/calibre-viewer.png

# every file is empty here
find %{buildroot}%{_datadir}/mime -maxdepth 1 -type f|xargs rm -f 

# packages aren't allowed to register mimetypes like this
rm -f %{buildroot}%{_datadir}/applications/{defaults.list,mimeinfo.cache}

desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-ebook-viewer.desktop
desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-gui.desktop
desktop-file-validate \
%{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop


mv %{buildroot}%{_datadir}/mime/packages/calibre-mimetypes \
	%{buildroot}%{_datadir}/mime/packages/calibre-mimetypes.xml

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
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}

# these are provided as separate packages
rm -rf %{buildroot}%{_libdir}/%{name}/{odf,cherrypy,pyPdf,encutils,cssutils}
rm -rf %{buildroot}%{_libdir}/%{name}/cal/utils/genshi
rm -rf %{buildroot}%{_libdir}/%{name}/cal/trac

# link to system fonts after we have deleted the non-free ones
# http://bugs.calibre-ebook.com/ticket/3832
mkdir -p %{buildroot}%{_datadir}/%{name}/fonts/prs500/
ln -s %{_datadir}/fonts/TTF/liberation/LiberationSans-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0003m_.ttf
ln -s %{_datadir}/fonts/TTF/liberation/LiberationSerif-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0011m_.ttf
ln -s %{_datadir}/fonts/TTF/liberation/LiberationMono-Regular.ttf \
	%{buildroot}%{_datadir}/%{name}/fonts/prs500/tt0419m_.ttf

# man pages
mv %{buildroot}%{_datadir}/%{name}/man %{buildroot}%{_mandir}

# move locales
mv %{buildroot}%{_datadir}/%{name}/localization/locales \
	%{buildroot}%{_datadir}/locale
for file in %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/messages.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/messages.mo \
	%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo
done;
for file in %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/iso639.mo; do
	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
	mv %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/iso639.mo \
	%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/%{name}_iso639.mo
done;
for file in %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/qt.qm; do
    lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
    mv $file %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/%{name}_$lang.qm
done;

# remove udev hack - it's not needed...
rm -f %{buildroot}%{_prefix}/lib/udev/rules.d/*

%find_lang %{name} --with-kde --all-name

# locales should be looked for in the proper place
%{__sed} -i -e "s:P('localization/locales:('/usr/share/locale:" \
	-e "s/messages.mo/calibre.mo/" \
	-e "s/iso639.mo/calibre_iso639.mo/" \
	%{buildroot}%{_libdir}/%{name}/%{name}/utils/localization.py

%{__rm} -f %{buildroot}%{_bindir}/%{name}-uninstall   

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang

%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE Changelog.yaml
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/locale/*/*/*.qm
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_mandir}/man1/*
%{python_sitelib}/init_calibre.py*
