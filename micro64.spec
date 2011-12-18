Name:		micro64
Version:	0.0.655
Release:	%mkrel 1
Summary:	Aimed to become the most accurate C64 Emulator
License:	Freeware
Group:		Emulators
URL:		http://micro64.de/
Source0:	http://micro64.de/downloads/%{name}-%{version}.zip
Source1:	micro64.png
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot

%description
The highly advanced successor of brotkaestchen (fr-051) from BeRo / farbrausch.

Currently it has 2 different VIC II emulation modes (both are half-cycle exact):
- single pixel dot clock exact (very accurate, slow)
- dynamic pixel block-wise (quite fast, even on slower machines).

Normally you shouldn't notice any differences, except in demos with a lot of
VIC II trickery. If your computer is fast enough you definitely should use
the accurate mode.

Status: Still under heavy development! Due to constant nagging, we decided
that it's time to prove that micro64 is not vaporware. Enjoy the current state
pre-release. Test stuff. Report bugs. New builds will appear from time to time.

%prep
%setup -q -n %{name}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Micro64
Comment=C64 emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_bindir}
%ifarch x86_64
%__install -m 755 %{name}_64 %{buildroot}%{_bindir}/%{name}
%else
%__install -m 755 %{name} %{buildroot}%{_bindir}/%{name}
%endif

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

