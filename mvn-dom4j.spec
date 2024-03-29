#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-dom4j
Version  : 1.1
Release  : 2
URL      : https://github.com/dom4j/dom4j/archive/dom4j-1-1.tar.gz
Source0  : https://github.com/dom4j/dom4j/archive/dom4j-1-1.tar.gz
Source1  : https://repo1.maven.org/maven2/dom4j/dom4j/1.1/dom4j-1.1.jar
Source2  : https://repo1.maven.org/maven2/dom4j/dom4j/1.1/dom4j-1.1.pom
Source3  : https://repo1.maven.org/maven2/dom4j/dom4j/1.6.1/dom4j-1.6.1.jar
Source4  : https://repo1.maven.org/maven2/dom4j/dom4j/1.6.1/dom4j-1.6.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause Plexus
Requires: mvn-dom4j-data = %{version}-%{release}
Requires: mvn-dom4j-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
These are XSL stylesheets for the DocBk XML DTD. (They would
also work for the DocBook DTD, modulo certain namecase problems
and the fact that there aren't (yet) any XSL implementations
that work with SGML source documents.)

%package data
Summary: data components for the mvn-dom4j package.
Group: Data

%description data
data components for the mvn-dom4j package.


%package license
Summary: license components for the mvn-dom4j package.
Group: Default

%description license
license components for the mvn-dom4j package.


%prep
%setup -q -n dom4j-dom4j-1-1

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-dom4j
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-dom4j/LICENSE.txt
cp src/doc/license.xml %{buildroot}/usr/share/package-licenses/mvn-dom4j/src_doc_license.xml
mkdir -p %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.1/dom4j-1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.1/dom4j-1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1/dom4j-1.6.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1/dom4j-1.6.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/dom4j/dom4j/1.1/dom4j-1.1.jar
/usr/share/java/.m2/repository/dom4j/dom4j/1.1/dom4j-1.1.pom
/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1/dom4j-1.6.1.jar
/usr/share/java/.m2/repository/dom4j/dom4j/1.6.1/dom4j-1.6.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-dom4j/LICENSE.txt
/usr/share/package-licenses/mvn-dom4j/src_doc_license.xml
