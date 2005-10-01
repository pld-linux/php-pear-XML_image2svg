%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	image2svg
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - image to SVG conversion
Summary(pl):	%{_pearname} - konwersja rysunków do SVG
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	4.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1881e3e89f552f7959ab4f0f7cf52cde
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/XML_image2svg/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class converts images, such as of the format JPEG, PNG and GIF to
a standalone SVG representation. The image is being encoded by the PHP
native encode_base64() function. You can use it to get back a complete
SVG file, which is based on a predefinded, easy adaptable template
file, or you can take the encoded file as a return value, using the
get() method. Due to the encoding by base64, the SVG files will
increase approx. 30% in size compared to the conventional image.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa konwertuje rysunki, takie formaty jak JPEG, PNG czy TIFF do
samodzielnej reprezentacji SVG. Rysunek jest kodowany przy u¿yciu
natywnej funkcji encode_base64() PHP. Mo¿esz z powrotem wróciæ do
kompletnego pliku SVG, który jest oparty na predefiniowanym, ³atwym do
zaadaptowania pliku tymczasowym, lub mo¿esz wzi±æ zakodowany plik jako
warto¶æ zwrotn±, u¿ywaj±c do metody get(). Poprzez zakodowanie przez
base64, pliki SVG s± ok. 30% wiêksze ni¿ konwencjonalne rysunki.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
cd ./%{php_pear_dir}/%{_class}
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
