%global tl_name interchar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Managing character class schemes in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/interchar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interchar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interchar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package manages character class schemes of XeTeX. Using this
package, you may switch among different character class schemes.
Migration commands are provided for make packages using this mechanism
compatible with each others.

