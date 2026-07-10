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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are provided as Metafont source.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources
%dir %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/README
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/CGA.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/agfa.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/amiga-PAL.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/amiga.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/chess.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/fselch15.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/fselch30.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/fselch34.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/fselch5mm.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkelch.mfj
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkfootbows.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkmakeneutral.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkparallel.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkscreengrid.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/pkshorten.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px150.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px17.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px20.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px21.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px23.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px25.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px29.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px31.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px33.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px41.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px45.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px49.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px53.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px57.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px63.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px700.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px71.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px72.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px79.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/px9.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/scan.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/screengrid.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/tt.mf
%doc %{_datadir}/texmf-dist/doc/fonts/bartel-chess-fonts/other-sources/turnboard.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-bishop.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-blackfield.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-chbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-equi.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-geo.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-king.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-knight.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-pawn.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-queen.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/elch-rook.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch11.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch13.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch14.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch16.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch20.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch24.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch32.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch36.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/fselch9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkbishop.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkblackfield.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch11.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch14.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch16.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkelch9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkgeo.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkking.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkknight.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkpawn.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkqueen.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bartel-chess-fonts/pkrook.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch11.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch13.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch14.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch16.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch20.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch24.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch32.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch36.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/fselch9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch11.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch14.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch16.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/pkelch9.tfm
