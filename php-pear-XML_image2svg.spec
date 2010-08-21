%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	image2svg
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - image to SVG conversion
Summary(pl.UTF-8):	%{_pearname} - konwersja rysunków do SVG
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	77c8e95bdfa451a0dab40f5fe6057307
URL:		http://pear.php.net/package/XML_image2svg/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php-pear-HTML_Template_IT
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(HTML/Template/IT.*)

%description
The class converts images, such as of the format JPEG, PNG and GIF to
a standalone SVG representation. The image is being encoded by the PHP
native encode_base64() function. You can use it to get back a complete
SVG file, which is based on a predefinded, easy adaptable template
file, or you can take the encoded file as a return value, using the
get() method. Due to the encoding by base64, the SVG files will
increase approx. 30% in size compared to the conventional image.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa konwertuje rysunki, takie formaty jak JPEG, PNG czy TIFF do
samodzielnej reprezentacji SVG. Rysunek jest kodowany przy użyciu
natywnej funkcji encode_base64() PHP. Możesz z powrotem wrócić do
kompletnego pliku SVG, który jest oparty na predefiniowanym, łatwym do
zaadaptowania pliku tymczasowym, lub możesz wziąć zakodowany plik jako
wartość zwrotną, używając do metody get(). Poprzez zakodowanie przez
base64, pliki SVG są ok. 30% większe niż konwencjonalne rysunki.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

rm .%{php_pear_dir}/package.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
