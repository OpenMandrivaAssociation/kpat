Name:		kpat
Version:	16.08.3
Release:	1
Epoch:		1
Summary:	Several patience card games
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kpatience/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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
Requires:	libkdegames-common >= 1:15.12.0
Conflicts:	kdegames4-devel < 1:4.5.71-0.svn1184269.2
Conflicts:	kdegames4-core < 1:4.9.80

%description -n kpat
KPatience is a relaxing card sorting game. To win the game a player has to
arrange a single deck of cards in certain order amongst each other.

%files -n kpat
%config %{_sysconfdir}/xdg/kpat.knsrc
%config %{_sysconfdir}/xdg/kcardtheme.knsrc
%{_bindir}/kpat
%{_libdir}/libkcardgame.so
%{_datadir}/applications/org.kde.kpat.desktop
%{_datadir}/kpat
%{_datadir}/kxmlgui5/kpat/kpatui.rc
%{_datadir}/config.kcfg/kpat.kcfg
%{_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/mime/packages/kpatience.xml
%doc %{_docdir}/*/*/kpat

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
