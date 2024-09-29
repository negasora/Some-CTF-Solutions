#!/usr/bin/env python3

from pwn import *

exe = ELF("spaceman_patched")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = True
DEBUG = True

HOST = ""
PORT = 1337

gdbscript = '''
c
'''

# make stack exec, jump to stack? make name exec jump to name?

if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)


r.interactive()
