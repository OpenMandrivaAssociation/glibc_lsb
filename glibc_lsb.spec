%define ld_ver 3
%define compat_ld_ver 2
%define	libname	%mklibname	glibc_lsb

Name:		glibc_lsb
Version:	2.4.7
Release:	17
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
install -d $RPM_BUILD_ROOT/%{_lib}
%ifarch %{ix86}
ln -sf ld-linux.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb.so.%{ld_ver}
ln -sf ld-linux.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb.so.%{compat_ld_ver}
%endif
%ifarch ppc
ln -sf ld-2.4.so $RPM_BUILD_ROOT/%{_lib}/ld-lsb-ppc32.so.%{ld_ver}
ln -sf ld-2.4.so $RPM_BUILD_ROOT/%{_lib}/ld-lsb-ppc32.so.%{compat_ld_ver}
%endif
%ifarch x86_64
ln -sf ld-linux-x86-64.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-x86-64.so.%{ld_ver}
ln -sf ld-linux-x86-64.so.2 $RPM_BUILD_ROOT/%{_lib}/ld-lsb-x86-64.so.%{compat_ld_ver}
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


%changelog
* Thu Apr 21 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.4.7-5
+ Revision: 656582
- remove obsolete rpm stuff
- from Stew Benedict:
  	o rework packaging for bi-arch support

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.4.7-4mdv2011.0
+ Revision: 219555
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.4.7-2mdv2008.0
+ Revision: 91266
- rebuild for 2008
- new license policy, correct license


* Fri Mar 02 2007 Stew Benedict <sbenedict@mandriva.com> 2.4.7-1mdv2007.0
+ Revision: 131335
- Import glibc_lsb

* Fri Mar 02 2007 Stew Benedict <sbenedict@mandriva.com> 2.4.7-1mdv2007.1
- LSB3.1, bump version
- fix symlink for ppc, there is no ld-linux.so...

* Fri Mar 31 2006 Stew Benedict <sbenedict@mandriva.com> 2.3.6-1mdk
- track the glibc version, requires lsb-core now

* Sat Apr 30 2005 Stew Benedict <sbenedict@mandriva.com> 2.3.4-2mdk
- restore LSB2.0 dynamic loaders links for LSB2/3 compatibility

* Sat Apr 23 2005 Stew Benedict <sbenedict@mandriva.com> 2.3.4-1mdk
- LSB3.0, bump version, URL

* Fri Jul 23 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.3.3-3mdk
- clean RPM_BUILD_ROOT (Christiaan Welvaart)

* Fri Jul 23 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.3.3-2mdk
- dynamic linker names change, add x86_64

* Sat Apr 03 2004 Stew Benedict <sbenedict@mandrakesoft.com> 2.3.3-1mdk
- rebuild, bump version

