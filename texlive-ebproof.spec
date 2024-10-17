Name:		texlive-ebproof
Version:	57544
Release:	2
Summary:	Formal proofs in the style of sequent calculus
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ebproof
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebproof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebproof.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ebproof.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands to typeset proof trees in the
style of sequent calculus and related systems. The commands
allow for writing inferences with any number of premises and
alignment of successive formulas on an arbitrary point. Various
options allow complete control over spacing, styles of
inference rules, placement of labels, etc. The package requires
expl3 and xparse.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ebproof
%{_texmfdistdir}/tex/latex/ebproof
%doc %{_texmfdistdir}/doc/latex/ebproof

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
