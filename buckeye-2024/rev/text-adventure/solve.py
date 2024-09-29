from pwn import *


r = remote("challs.pwnoh.io", 13376)

commands = b"""
enter
take torch
go right
cross
grab rope
go back
go back
go middle
descend
go right
use rope
take sword
go back
go back
go back
go back
go left
cut the webs
take key
go back
go back
go middle
descend
go left
unlock door
reach through the crack in the rocks
the crack in the rocks concealing the magical orb with the flag
"""

for line in commands.splitlines():
    line = line.strip()
    if len(line) == 0:
        continue
    print(r.recvuntil(b'>').decode())
    r.sendline(line)

r.interactive()
