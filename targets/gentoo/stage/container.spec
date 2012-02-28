[collect stage3-derivative.spec]
[collect ../steps/container.spec]

[section metro]

class: chroot

[section target]

type: image

[section path]

chroot: $[path/work]

[section files]

motd: [

 >>> Template:                      $[target/name]
 >>> Technology:                    $[target/realname]
 >>> Version:                       $[target/version]
 >>> Created by:                    $[local/author]

 >>> Send suggestions, improvements, bug reports relating to...

 >>> This template:                 $[local/author]
 >>> Funtoo Linux (general):        Funtoo Linux (http://www.funtoo.org)
 >>> Gentoo Linux (general):        Gentoo Linux (http://www.gentoo.org)
 >>> Container technology:          $[target/url]

 NOTE: This message can be removed by deleting /etc/motd.

]
