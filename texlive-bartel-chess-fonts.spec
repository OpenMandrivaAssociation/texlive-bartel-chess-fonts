# revision 20619
# category Package
# catalog-ctan /fonts/bartel-chess-fonts
# catalog-date 2010-11-29 08:56:06 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-bartel-chess-fonts
Version:	20101129
Release:	5
Summary:	A set of fonts supporting chess diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bartel-chess-fonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bartel-chess-fonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bartel-chess-fonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are provided as MetaFont source.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-bishop.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-blackfield.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-chbase.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-equi.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-geo.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-king.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-knight.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-pawn.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-queen.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-rook.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch10.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch11.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch12.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch13.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch14.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch16.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch17.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch20.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch24.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch32.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch36.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch6.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch7.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch8.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch9.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkbase.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkbishop.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkblackfield.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch10.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch11.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch12.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch14.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch16.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch8.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch9.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkgeo.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkking.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkknight.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkpawn.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkqueen.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkrook.mf
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch10.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch11.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch12.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch13.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch14.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch16.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch17.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch20.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch24.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch32.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch36.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch6.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch7.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch8.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch9.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch10.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch11.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch12.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch14.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch16.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch8.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch9.tfm
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/README
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/CGA.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/agfa.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/amiga-PAL.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/amiga.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/chess.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch15.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch30.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch34.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch5mm.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkelch.mfj
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkfootbows.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkmakeneutral.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkparallel.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkscreengrid.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkshorten.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px150.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px17.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px20.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px21.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px23.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px25.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px29.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px31.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px33.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px41.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px45.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px49.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px53.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px57.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px63.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px700.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px71.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px72.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px79.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px9.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/scan.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/screengrid.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/tt.mf
%doc %{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/turnboard.mf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101129-2
+ Revision: 749450
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101129-1
+ Revision: 717884
- texlive-bartel-chess-fonts
- texlive-bartel-chess-fonts
- texlive-bartel-chess-fonts
- texlive-bartel-chess-fonts
- texlive-bartel-chess-fonts

