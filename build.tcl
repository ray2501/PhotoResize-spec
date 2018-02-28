#!/usr/bin/tclsh

set arch "x86_64"
set base "photoresize-0.1_git20170924"

set var2 [list git clone https://github.com/auriocus/PhotoResize.git $base]
exec >@stdout 2>@stderr {*}$var2

cd $base

set var2 [list git checkout 53aca14bb0d6da05ac286c37c9ea4de14d595cc3]
exec >@stdout 2>@stderr {*}$var2

set var2 [list git reset --hard]
exec >@stdout 2>@stderr {*}$var2

file delete -force .git

cd ..

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb photoresize.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete -force $base.tar.gz

