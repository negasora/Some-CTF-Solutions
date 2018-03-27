from pwn import *



r = ""
ss = 0

keys = []

def initconn():
    global r, ss
    r = remote("web.chal.csaw.io", 4333, level='error')
    p = 251
    g = 6
    a = 17
    A = pow(g, a, p)
    r.sendline(chr(A))
    B = int(r.read().encode("hex"),16)
    ss = pow(B, a, p)


def encdec(s):
    global ss
    out = ""
    for i in s:
        out += chr(ord(i) ^ ss)
    return out

def visit(s):
    global r
    initconn()
    r.send(encdec(s))
    #r.interactive()
    print encdec(r.read())
    #handle(encdec(r.readall()))


def handle(s):
    print s
    lines = s.split("\n")
    if lines[0][0]!= "P":
        print "AAAAAAAAAAAAAAA"
    for line in lines[1:]:
        line = line.replace("\r", '')
        if "congrats" in line.lower():
            print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
            pass  
        la = line.split("\t")
        if la[0] == "T":
            print la[1]
        elif la[0] == 'P':
            print la[1]
            visit(la[1])
        elif la[0] == 'C':
            keys.append(int(la[1][4:]))

visit("/run_client\thost:45.33.26.124\tport:31337")
#visit("/reset")

print encdec(r.readall())

