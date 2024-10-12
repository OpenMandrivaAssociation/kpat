#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
# https://bugs.kde.org/show_bug.cgi?id=407864
%global optflags %{optflags} -DNDEBUG

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-kpat
Version:	24.08.2
Release:	%{?git:0.%{git}.}1
Summary:	Several patience card games
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kpatience/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kpat/-/archive/%{gitbranch}/kpat-%{gitbranchd}.tar.bz2#/kpat-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kpat-%{version}.tar.xz
%endif
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(libfreecell-solver)
BuildRequires:	pkgconfig(libblack-hole-solver)
Requires:	plasma6-libkdegames-common

%description
KPatience is a relaxing card sorting game. To win the game a player has to
arrange a single deck of cards in certain order amongst each other.

%files -f %{name}.lang
%{_datadir}/knsrcfiles/kpat.knsrc
%{_datadir}/knsrcfiles/kcardtheme.knsrc
%{_datadir}/qlogging-categories6/kpat.renamecategories
%{_datadir}/qlogging-categories6/kpat.categories
%{_bindir}/kpat
%{_libdir}/libkcardgame.so
%{_datadir}/applications/org.kde.kpat.desktop
%{_datadir}/kpat
%{_datadir}/metainfo/org.kde.kpat.appdata.xml
%{_datadir}/config.kcfg/kpat.kcfg
%{_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/mime/packages/kpatience.xml
%{_mandir}/man6/kpat.6*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kpat-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html --with-man --all-name
