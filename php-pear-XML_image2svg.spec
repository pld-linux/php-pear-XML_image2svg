%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       image2svg
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Image to SVG conversion
Summary(pl):	%{_pearname} - Konwersja rysunków do SVG
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
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

%description -l pl
Ta klasa konwertuje rysunki, takie formaty jak JPEG, PNG czy TIFF do
samodzielnej reprezentacji SVG. Rysunek jest kodowany przy u¿yciu
natywnej funkcji encode_base64() PHP. Mo¿esz z powrotem wróciæ do
kompletnego pliku SVG, który jest oparty na predefiniowanym, ³atwym do
zaadaptowania pliku tymczasowym, lub mo¿esz wzi±æ zakodowany plik jako
warto¶æ zwrotn±, u¿ywaj±c do metody get(). Poprzez zakodowanie przez
base64, pliki SVG s± ok. 30% wiêksze ni¿ konwencjonalne rysunki.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%{php_pear_dir}/%{_class}/*.php
