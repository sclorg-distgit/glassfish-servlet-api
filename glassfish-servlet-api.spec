%{?scl:%scl_package glassfish-servlet-api}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global artifactId javax.servlet-api

Name:           %{?scl_prefix}glassfish-servlet-api
Version:        3.1.0
Release:        6%{?dist}
Summary:        Java Servlet API
License:        (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:            http://servlet-spec.java.net
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.servlet-api-3.1.0 javax.servlet-api-3.1.0
# tar cvJf javax.servlet-api-3.1.0.tar.xz javax.servlet-api-3.1.0/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_maven}jvnet-parent
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_maven}maven-source-plugin


%description
The javax.servlet package contains a number of classes 
and interfaces that describe and define the contracts between 
a servlet class and the runtime environment provided for 
an instance of such a class by a conforming servlet container.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
%pom_remove_plugin :maven-remote-resources-plugin
cp -p %{SOURCE1} .
# README contains also part of javax.servlet-api license
cp -p src/main/resources/META-INF/README .
%mvn_file :%{artifactId} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE-2.0.txt README

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt README

%changelog
* Mon May 11 2015 Mat Booth <mat.booth@redhat.com> - 3.1.0-6
- Resolves: rhbz#1219013 - Fails to build from source

* Tue May 20 2014 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-5
- Fix name of jars to be pkg_name instead of name.

* Thu May 15 2014 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-4
- Properly sclize.

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.1.0-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 gil cattaneo <puntogil@libero.it> - 3.1.0-1
- Update to 3.1.0

* Sat Mar 09 2013 David Xie <david.scriptfan@gmail.com> - 3.1-0.1.b07
- Initial version of package
