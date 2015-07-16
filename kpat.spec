Name:		kpat
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Several patience card games
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/kpatience/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	libkdegames-common
Conflicts:	kdegames4-devel < 1:4.5.71-0.svn1184269.2
Conflicts:	kdegames4-core < 1:4.9.80
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF5CoreAddo)                                                                     
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5WidgetsAons)                                                                  
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5DBusAddo)                                                                     
BuildRequires:  cmake(KF5Declarate)                                                                    
BuildRequires:  cmake(KF5I18n)                                                                         
BuildRequires:  cmake(KF5GuiAddon)                                                                     
BuildRequires:  cmake(KF5ConfigWiets)                                                                  
BuildRequires:  cmake(KF5ItemView)                                                                     
BuildRequires:  cmake(KF5IconThem)                                                                     
BuildRequires:  cmake(KF5Completi)                                                                     
BuildRequires:  cmake(KF5TextWidgs)                                                                    
BuildRequires:  cmake(KF5XmlGui)                                                                       
BuildRequires:  cmake(KF5KIO)                                                                          
BuildRequires:  cmake(KF5NotifyCoig)                                                                   
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:	cmake(KF5KDEGames)

%description -n kpat
KPatience is a relaxing card sorting game. To win the game a player has to
arrange a single deck of cards in certain order amongst each other.

%files -n kpat
%{_bindir}/kpat                                                                                        
%{_libdir}/libkcardgame.so                                                                             
%{_datadir}/applications/org.kde.kpat.desktop                                                          
%{_datadir}/apps/kpat  
%{_datadir}/kxmlgui5/kpat/kpatui.rc
%{_datadir}/config.kcfg/kpat.kcfg                                                                      
%{_datadir}/config/kpat.knsrc                                                                          
%{_datadir}/config/kcardtheme.knsrc                                                                    
%doc %{_docdir}/*/*/kpat                                                                               
%{_iconsdir}/hicolor/*/apps/kpat.png                                                                   
%{_datadir}/mime/packages/kpatience.xml     

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

