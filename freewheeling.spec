Summary:	Freewheeling Live Looper
Name:		freewheeling
Version:	0.6.4
Release:	3
License:	GPL v2
Group:		Applications
Source0:	https://github.com/free-wheeling/freewheeling/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7a76624759929fe819d3a0d0dc8c0bb3
Patch0:		config.patch
Patch1:		fluidsynth2.patch
URL:		https://github.com/free-wheeling/freewheeling/
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fluidsynth-devel
BuildRequires:	freetype-devel
BuildRequires:	gnutls-openssl-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	libogg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freewheeling provides a highly configurable, intuitive, and fluid user
interface for instrumentalists to capture audio loops in real-time.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{rpmcflags} -I/usr/include/SDL"
export CXXFLAGS="%{rpmcxxflags} -I/usr/include/SDL"
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
%doc AUTHORS ChangeLog THANKS TUNING
%doc data/config-help.txt examples
%attr(755,root,root) %{_bindir}/fweelin
%{_datadir}/fweelin
