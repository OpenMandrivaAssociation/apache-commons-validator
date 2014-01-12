%{?_javapackages_macros:%_javapackages_macros}
%global short_name      commons-validator

Name:             apache-%{short_name}
Version:          1.4.0
Release:          6.1%{?dist}
Summary:          Apache Commons Validator

License:          ASL 2.0
URL:              http://commons.apache.org/validator/
Source0:          http://www.apache.org/dist/commons/validator/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    maven-local
Requires:         java >= 1:1.6.0
Requires:         jpackage-utils

%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-validator %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Aug 06 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.0-6
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-2
- Install NOTICE file with javadoc package

* Fri Oct 19 2012 Chris Spike <spike@fedoraproject.org> 1.4.0-1
- Updated to 1.4.0
- Switched build tool from ant to maven
- Updated to latest java packaging guidelines
- Dropped oro BR/R

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Stanislav Ochotnicky <sochotnicky@redhat.com>- 1.3.1-8
- Fix tests after junit update

* Sat Jan 14 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-7
- Tweak source encoding to fix build with Java 1.7.
- Drop versioned jars and javadoc dir.
- Drop no longer needed javadoc Obsoletes.
- Crosslink with local JDK API docs.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3.1-5
- Change oro to jakarta-oro in BR/R

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Chris Spike <chris.spike@arcor.de> 1.3.1-3
- Moved junit tests to check section

* Sat Oct 2 2010 Chris Spike <chris.spike@arcor.de> 1.3.1-2
- Rename and rebase from jakarta-commons-validator
