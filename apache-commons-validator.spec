Name:		apache-commons-validator
Epoch:		1
Version:	1.11.0
Release:	1
Summary:	Framework to define validation rules for user input
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-validator/
Source0:	https://github.com/apache/commons-validator/archive/refs/tags/rel/commons-validator-%{version}.tar.gz#/commons-validator-%{version}.tar.gz

BuildArch:	noarch
# The site checkout profile is active when site-content is absent, and
# antrun is on the sysjar keep list.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
BuildRequires:	mvn(org.apache:apache:pom::)
BuildRequires:	mvn(commons-beanutils:commons-beanutils)
BuildRequires:	mvn(commons-digester:commons-digester)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(commons-collections:commons-collections)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-validator --link %{name} --alias org.apache.commons:commons-validator

Obsoletes:	%{name}-javadoc < %{epoch}:%{version}-%{release}

%description
Apache Commons Validator checks user input against declarative rules.
1.11.0 needs Java 8. ValidatorException and CheckDigitException gain
constructors that keep the cause and format the message. Domain
checks drop several retired top-level domains. Tests are skipped.

%prep
%autosetup -n commons-validator-rel-commons-validator-%{version}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt README.md
