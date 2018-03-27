from pwn import *



r = ""
ss = 0

keys = []

def initconn():
    global r, ss
    r = remote("web.chal.csaw.io", 433, level='error')
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
    handle(encdec(r.readall()))


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
        else:
            print la

#visit("/")
visit("/imnotabusive")
#print handle(encdec(r.readall()))


f = [ord(i) for i in "UsjQW5nkTxZ6Vuh4qDPuNS0vLkRBUGx93oIdtVSDMtw25A==".decode('base64')]
o = ""
print keys
for i in xrange(len(keys)):
    o = keys[i] ^ f[i%len(f)]
    f[i%len(f)] = o

print ''.join([chr(i) for i in f])


