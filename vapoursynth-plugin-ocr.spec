Summary:	Tesseract-based OCR plugin for Vapoursynth
Summary(pl.UTF-8):	Oparta na Tesserakcie wtyczka OCR dla programu Vapoursynth
Name:		vapoursynth-plugin-ocr
Version:	3
Release:	1
# it was vapoursynth.spec subpackage up to 54
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	https://github.com/vapoursynth/vs-ocr/archive/R%{version}/vs-ocr-R%{version}.tar.gz
# Source0-md5:	2372d12d4c7061258709106cf64c6881
URL:		https://github.com/vapoursynth/vs-ocr
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	vapoursynth-devel >= 55
BuildRequires:	tesseract-devel >= 4.1.1
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vapoursynth filter that performs optical character recognition on
video frames.

%description -l pl.UTF-8
Filtr Vapoursynth dokonujący optycznego rozpoznawania znaków w
klatkach obrazu.

%prep
%setup -q -n vs-ocr-R%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE docs/ocr.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libocr.so
