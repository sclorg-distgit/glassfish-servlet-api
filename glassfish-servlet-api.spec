%{?scl:%scl_package glassfish-servlet-api}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global artifactId javax.servlet-api

Name:           %{?scl_prefix}glassfish-servlet-api
Version:        3.1.0
Release:        9.1%{?dist}
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
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{artifactId}-%{version}
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-javadoc-plugin
cp -p %{SOURCE1} .
# README contains also part of javax.servlet-api license
cp -p src/main/resources/META-INF/README .
%mvn_file :%{artifactId} %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_alias : javax.servlet:servlet-api
%mvn_alias : org.apache.geronimo.specs:geronimo-servlet_3.0_spec
%mvn_alias : org.eclipse.jetty.orbit:javax.servlet
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc README
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc README
%doc LICENSE-2.0.txt

%changelog
* Tue Jun 23 2015 Mat Booth <mat.booth@redhat.com> - 3.1.0-9.1
- Import latest from Fedora

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 3 2015 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-8
- Add alias for org.eclipse.jetty.orbit:javax.servlet.
- Fix javadoc compilation.

* Fri Feb 13 2015 gil cattaneo <puntogil@libero.it> 3.1.0-7
- introduce license macro

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-6
- Add alias for Geronimo servlet API

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 5 2014 Alexander Kurtakov <akurtako@redhat.com> 3.1.0-4
- Add javax.servlet:servlet-api alias.

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.1.0-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 gil cattaneo <puntogil@libero.it> - 3.1.0-1
- Update to 3.1.0

* Sat Mar 09 2013 David Xie <david.scriptfan@gmail.com> - 3.1-0.1.b07
- Initial version of package
