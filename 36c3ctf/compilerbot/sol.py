from pwn import *


r = remote("88.198.154.157", 8011)


print(r.read())

r.sendline("return 0;")
print(r.read())
