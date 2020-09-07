# https://bugs.kde.org/show_bug.cgi?id=407854
%global optflags %{optflags} -DNDEBUG

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kpat
Version:	20.08.1
Release:	1
Epoch:		1
Summary:	Several patience card games
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kpatience/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	shared-mime-info
BuildRequires:	pkgconfig(libfreecell-solver)
Requires:	libkdegames-common >= 1:15.12.0
Conflicts:	kdegames4-devel < 1:4.5.71-0.svn1184269.2
Conflicts:	kdegames4-core < 1:4.9.80

%description
KPatience is a relaxing card sorting game. To win the game a player has to
arrange a single deck of cards in certain order amongst each other.

%files -f %{name}.lang
%{_sysconfdir}/xdg/kpat.knsrc
%{_sysconfdir}/xdg/kcardtheme.knsrc
%{_datadir}/qlogging-categories5/kpat.categories
%{_bindir}/kpat
%{_libdir}/libkcardgame.so
%{_datadir}/applications/org.kde.kpat.desktop
%{_datadir}/kpat
%{_datadir}/kxmlgui5/kpat/kpatui.rc
%{_datadir}/metainfo/org.kde.kpat.appdata.xml
%{_datadir}/config.kcfg/kpat.kcfg
%{_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/mime/packages/kpatience.xml
%{_mandir}/man6/kpat.6*

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html --with-man --all-name
