%define ld_ver 3
%define compat_ld_ver 2
%define	libname	%mklibname	glibc_lsb

Name:		glibc_lsb
Version:	2.4.7
Release:	5
Group:		System/Libraries
Summary:	LSB dynamic loader links
License:	Freely redistributable without restriction
URL:		http://www.linuxbase.org/spec

Requires:	lsb-core >= 3.1

%description
Provides ld-lsb* dynamic loader links for LSB compliance

%package -n	%{libname}
Group:		System/Libraries
Summary:	LSB dynamic loader links
%rename		glibc_lsb

%description -n %{libname}
Provides ld-lsb* dynamic loader links for LSB compliance

%prep

%build

%install
install -d %{buildroot}/%{_lib}
%ifarch %{ix86}
ln -sf ld-linux.so.2 %{buildroot}/%{_lib}/ld-lsb.so.%{ld_ver}
ln -sf ld-linux.so.2 %{buildroot}/%{_lib}/ld-lsb.so.%{compat_ld_ver}
%endif
%ifarch ppc
ln -sf ld-2.4.so %{buildroot}/%{_lib}/ld-lsb-ppc32.so.%{ld_ver}
ln -sf ld-2.4.so %{buildroot}/%{_lib}/ld-lsb-ppc32.so.%{compat_ld_ver}
%endif
%ifarch x86_64
ln -sf ld-linux-x86-64.so.2 %{buildroot}/%{_lib}/ld-lsb-x86-64.so.%{ld_ver}
ln -sf ld-linux-x86-64.so.2 %{buildroot}/%{_lib}/ld-lsb-x86-64.so.%{compat_ld_ver}
%endif

export DONT_SYMLINK_LIBS=1

%files -n %{libname}
%ifarch %{ix86}
/%{_lib}/ld-lsb.so.%{ld_ver}
/%{_lib}/ld-lsb.so.%{compat_ld_ver}
%endif
%ifarch ppc
/%{_lib}/ld-lsb-ppc32.so.%{ld_ver}
/%{_lib}/ld-lsb-ppc32.so.%{compat_ld_ver}
%endif
%ifarch x86_64
/%{_lib}/ld-lsb-x86-64.so.%{ld_ver}
/%{_lib}/ld-lsb-x86-64.so.%{compat_ld_ver}
%endif
