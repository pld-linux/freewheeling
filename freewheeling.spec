# TODO: system Vera font?
Summary:	Freewheeling Live Looper
Summary(pl.UTF-8):	Freewheeling - narzędzie do nagrywania pętli dźwiękowych w czasie rzeczywistym
Name:		freewheeling
Version:	0.6.6
Release:	2
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/free-wheeling/freewheeling/releases
Source0:	https://github.com/free-wheeling/freewheeling/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7ab4a2e6a9b46bff01f799f732f3e4c0
Patch0:		config.patch
URL:		https://github.com/free-wheeling/freewheeling/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_gfx-devel >= 1.2
BuildRequires:	SDL_ttf-devel >= 1.2
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	fluidsynth-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	libogg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	nettle-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freewheeling provides a highly configurable, intuitive, and fluid user
interface for instrumentalists to capture audio loops in real-time.

%description -l pl.UTF-8
Freewheeling udostępnia w dużym stopniu konfigurowalny, intuicyjny
interfejs użytkownika dla instrumentalistów, służący do nagrywania
pętli dźwiękowych w czasie rzeczywistym.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--enable-fluidsynth

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog THANKS TUNING data/config-help.txt examples
%attr(755,root,root) %{_bindir}/fweelin
%{_datadir}/fweelin
