%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define tarname photoresize

Name:          tcl-photoresize
Summary:       For Tcl to resize/resample photo images
Version:       0.1_git20170924
Release:       0
License:       MIT
Group:         Development/Libraries/Tcl
Source:        %{tarname}-%{version}.tar.gz
URL:           https://github.com/auriocus/PhotoResize
BuildRequires: autoconf
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: tcl-devel >= 8.4
BuildRequires: tk-devel >= 8.4
Requires:      tcl >= 8.4
Requires:      tk >= 8.4
BuildRoot:     %{buildroot}

%description
A single-purpose extension for Tcl to resize/resample photo images.

%prep
%setup -q -n %{tarname}-%{version}

%build
autoconf
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{tarname}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}

