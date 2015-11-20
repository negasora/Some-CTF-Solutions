#!/usr/bin/env python
# original author: 193s
# modified by negasora
from modular_sqrt import modular_sqrt
import string
from sys import exit


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

bytes_to_long = lambda s: int(s.encode('hex'), 16)
long_to_bytes = lambda l: ('%x'%l).decode('hex')

n = 20313365319875646582924758840260496108941009525871463319046021451803402705157052789599990588403
e = 1404119484958500351776
c = 4104314974842034312729644734009867622818315323910143873563666990448837112322264379294617825939
p = 164184701914508585475304431352949988726937945387
q = 123722643358410276082662590855480232574295214169
assert n == p*q

## enumerate all possible m = FLAG % n

list_m = set() # list of all possible m's

_d = modinv(e / (2**5), (p-1)*(q-1))

def dec(t, i):
  if i == 5:
    mm = pow(t, _d, n)
    if pow(mm, e, n) == c: list_m.add(mm)
  else:
    mp = modular_sqrt(t, p)
    mq = modular_sqrt(t, q)
    _, yp, yq = egcd(p, q)
    r = (yp*p*mq + yq*q*mp) % n
    s = (yp*p*mq - yq*q*mp) % n
    m1, m2, m3, m4 = r, s, n-r, n-s

    dec(m1, i+1)
    dec(m2, i+1)
    dec(m3, i+1)
    dec(m4, i+1)
dec(c, 0)

charset = string.printable


f = open("maybes", "ab")
for m in list_m:
	f.write(str(m)+'\n')
	print m
	print len(str(m))
f.close()



