Name:		texlive-interchar
Version:	36312
Release:	2
Summary:	Managing character class schemes in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/interchar
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interchar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interchar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package manages character class schemes of XeTeX. Using
this package, you may switch among different character class
schemes. Migration commands are provided for make packages
using this mechanism compatible with each others.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/interchar
%doc %{_texmfdistdir}/doc/xelatex/interchar

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
