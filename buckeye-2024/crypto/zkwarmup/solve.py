from math import gcd
import random
import time
#from flag import flag

from pwn import remote



r = remote('challs.pwnoh.io', 13421)

r.recvuntil(b'n = ')
n = int(r.recvline().strip())

r.recvuntil(b'y = ')
y = int(r.recvline().strip())

random.seed(int(time.time()))
x = random.randrange(1, n)
assert y == pow(x, 2, n), 'y random mismatch'


round_num = 0
for z in range(2, 130):
    print(f'Round {round_num}')
    round_num += 1
    b = random.randrange(2)
    z_sq = pow(z, 2)
    if b == 0:
        s = ((pow(y, -1, n)*z_sq) % n)
    else:
        s = z_sq

    r.sendlineafter(b'Provide s: ', str(s).encode())

    r.recvuntil(b'b = ')
    assert b == int(r.recvline().strip()), 'b random mismatch'

    r.sendlineafter(b'Provide z: ', str(z).encode())

    assert b'Verification passed' in r.recvline()

r.interactive()
