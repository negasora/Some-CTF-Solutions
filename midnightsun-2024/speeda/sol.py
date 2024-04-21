from pwn import *

context.terminal = ['kitty']

r = gdb.debug('./speed_a')


r.write(b'\xff'*0x8000) # why is this breaking? stack isn't growing idk


r.interactive()
