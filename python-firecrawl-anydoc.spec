%undefine _debugsource_packages

# The sdist Cargo.lock still lists the node and wasm crates, which are
# not in the Python sdist, so `cargo vendor --locked` refuses to run.
# Recreate the vendor archive after a version bump:
#   tar xf firecrawl_anydoc-VERSION.tar.gz && cd firecrawl_anydoc-VERSION
#   cargo vendor vendor
#   tar cJf python-firecrawl-anydoc-VERSION-vendor.tar.xz vendor Cargo.lock
#   abb store python-firecrawl-anydoc-VERSION-vendor.tar.xz

Name:		python-firecrawl-anydoc
Version:	0.2.4
Release:	1
Summary:	Convert office documents and PDF files to Markdown
License:	MIT
Group:		Development/Python
URL:		https://github.com/firecrawl/anydoc
Source0:	https://files.pythonhosted.org/packages/source/f/firecrawl-anydoc/firecrawl_anydoc-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	cargo
BuildRequires:	rust-packaging

%description
firecrawl-anydoc converts Word, PowerPoint, Excel, OpenDocument, RTF,
EPUB, CSV, and PDF files to GitHub-flavored Markdown. The distribution
name is firecrawl-anydoc; the import name is anydoc. Hermes uses it
when read_file opens a PDF or office document. Hosted OCR is optional
and is not required to import the module.

%prep -a
tar -xf %{SOURCE1}
%cargo_prep -v vendor

%build -p
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true

%build -a
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{python_sitearch}/anydoc
%{python_sitearch}/firecrawl_anydoc-%{version}.dist-info
