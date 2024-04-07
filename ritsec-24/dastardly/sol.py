from pwn import *


r = remote("ctf.ritsec.club", 30984)



keys = [
    b'0000000000000000',
    b'FFFFFFFFFFFFFFFF',
    b'E1E1E1E1F0F0F0F0',
    b'1E1E1E1E0F0F0F0F',
]

flag_hex = b'28e3a0ff9089aecc83465e470624a89253a1aac856a4f7ff08b4648b7c5eff9aa41a0dd1c7fc15995382dc3149dfcccf82241fb566fb5a0382241fb566fb5a03'
r.sendlineafter(b'(in hex)', keys[2])
r.sendlineafter(b'(in hex)', flag_hex)

r.interactive()

# RS{W0W_TH1S_K3YSP4C3_1S_4S_FL4T_4S_34RTH}
