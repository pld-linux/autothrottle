Summary:	autothrottle throttles your CPU
Summary(pl.UTF-8):   autothrottle - regulacja prędkości procesora
Name:		autothrottle
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.metalhead.ws/cbin/%{name}.tar.gz
# Source0-md5:	05cf1c9bf50a6cbf762f2ecd6ff0a2cc
URL:		http://www.metalhead.ws/cbin/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autothrottle is a daemon that throttles your CPU according to the
system load. It can be used with both ACPI and CPUfreq throttling.

%description -l pl.UTF-8
Autothrottle jest demonem, który reguluje prędkość procesora zależnie
od obciążenia systemu. Może być używany poprzez ACPI oraz CPUfreq.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -DTEST"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%{_mandir}/man1/*.1*
