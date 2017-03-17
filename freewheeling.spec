
%define	commit	4a03065f9d2f520cbd37dd560b4cae5685418153

Summary:	Freewheeling Live Looper
Name:		freewheeling
Version:	0.6.1
Release:	0.git.2
License:	GPL v2
Group:		Applications
Source0:	https://github.com/free-wheeling/freewheeling/archive/%{commit}/%{name}-%{commit}.tar.gz
# Source0-md5:	ac66a2eecd4992ae0e377458cb529448
Patch0:		format_string.patch
Patch1:		destdir.patch
Patch2:		config.patch
Patch3:		double_free.patch
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
%setup -q -n %{name}-%{commit}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

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
