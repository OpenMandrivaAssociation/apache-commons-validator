%global base_name       validator
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.3.1
Release:          6
Summary:          Apache Commons Validator
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch

BuildRequires:    java-devel >= 0:1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    oro
BuildRequires:    junit
Requires:         apache-commons-beanutils
Requires:         apache-commons-digester
Requires:         apache-commons-logging
Requires:         oro
Requires:         java >= 0:1.6.0
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# This should go away with F-17
Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:1.3.1-2

%description
A common issue when receiving data either electronically or from user input is 
verifying the integrity of the data. This work is repetitive and becomes even 
more complicated when different sets of validation rules need to be applied to 
the same set of data based on locale for example. Error messages may also vary 
by locale. This package attempts to address some of these issues and speed 
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
# This should go away with F-17
Obsoletes:        jakarta-%{short_name}-javadoc < 0:1.3.1-2

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

%build
# TODO: Use Maven for building as soon as upstream provides proper build.xml. 
#       Currently upstream build.xml uses antrun plugin to build, so downloads 
#       during build process can't be prohibited.

export CLASSPATH=$(build-classpath \
                   apache-commons-logging \
                   apache-commons-digester \
                   apache-commons-beanutils \
                   junit \
                   oro )

ant -Dskip.download=true -Dbuild.sysclasspath=first dist

%check
export CLASSPATH=$(build-classpath \
                   apache-commons-logging \
                   apache-commons-digester \
                   apache-commons-beanutils \
                   junit \
                   oro )

ant -Dskip.download=true -Dbuild.sysclasspath=first test

%install
rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*

%files javadoc
%defattr(-,root,root,-)
%doc LICENSE.txt
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

