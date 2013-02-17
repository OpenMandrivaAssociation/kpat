Name:		kpat
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	Several patience card games
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kpatience/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	libkdegames-common
Conflicts:	kdegames4-devel < 1:4.5.71-0.svn1184269.2
Conflicts:	kdegames4-core < 1:4.9.80

%description -n kpat
KPatience is a relaxing card sorting game. To win the game a player has to
arrange a single deck of cards in certain order amongst each other.

%files -n kpat
%{_kde_bindir}/kpat
%{_kde_libdir}/libkcardgame.so
%{_kde_applicationsdir}/kpat.desktop
%{_kde_appsdir}/kpat
%{_kde_datadir}/config.kcfg/kpat.kcfg
%{_kde_configdir}/kpat.knsrc
%{_kde_configdir}/kcardtheme.knsrc
%{_kde_docdir}/*/*/kpat
%{_kde_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/mime/packages/kpatience.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package
- Update files

