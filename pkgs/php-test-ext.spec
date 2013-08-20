
%global github_version     1.0

%global composer_vendor    test
%global composer_project   ext

Name:       php-%{composer_vendor}-%{composer_project}
Version:    %{github_version}
Release:    1%{?dist}
Summary:    test case

License:    BSD
URL:        https://github.com/siwinski/php-composer-rpms

BuildArch:  noarch

BuildRequires:  php-composer

%description
test case
WARNING: This is just a development RPM.  Please submit issues at
         https://github.com/siwinski/php-composer-rpms/issues and prefix
         your issue title with "[%name] ".


%prep
[ -e %{name}-%{version} ]  && rm -rf %{name}-%{version}
mkdir %{name}-%{version} && cd %{name}-%{version}
cat > app.php <<EOL
Well, this is our app that wants some composer deps
EOL

# minimal template, just with require section
cat > composer.json <<EOL
{
    "require" : {
        "sabre/dav" : "1.8.*"
    }
}
EOL


%build
# Empty build section, nothing to build


%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_datadir}/php/compsertestapp
install -pm 644 app.php %{buildroot}%{_datadir}/php/compsertestapp
install -pm 644 composer.json %{buildroot}%{_datadir}/php/compsertestapp

# now pull in specified deps - this creates the vendor dir
%{composer_install} --no-package-dir --verbose
cp -a vendor %{buildroot}%{_datadir}/php/compsertestapp


%files
%{_datadir}/php/compsertestapp


%changelog

