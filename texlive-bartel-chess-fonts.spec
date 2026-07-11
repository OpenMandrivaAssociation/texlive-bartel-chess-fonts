%global tl_name bartel-chess-fonts
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A set of fonts supporting chess diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bartel-chess-fonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bartel-chess-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bartel-chess-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are provided as Metafont source.

