#!/usr/bin/env python

from Crypto.Util.number import *
#from flag import FLAG




# real flag is 32 bytes long (makes file sizes match) (contents don't matter here, just making numbers line up)
FLAG = b"A"*32



def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n


# f is list of 1 and 0, begins with 0
f = [int(x) for x in bin(int(FLAG.hex(), 16))[2:]]

f.insert(0, 0)

f_final = [i for i in f]
for i in range(len(f)-1): f[i] += f[i+1]
a = nextPrime(len(f)) # 257
b = nextPrime(a) # 263


# g = f*a
# h = f*b 
g, h = [[_ for i in range(x) for _ in f] for x in [a, b]]


c = nextPrime(len(f) >> 2) # 67


g_final = [i for i in g]

for _ in [g, h]:
    for __ in range(c): _.insert(0, 0) # pad beginning of g and h with c zeros
    for i in range(len(_) -  c): _[i] += _[i+c] # add the next member to all elements, stopping at the -67th



g, h = [int(''.join([str(_) for _ in __]), 5) for __ in [g, h]] # concat list members, parse as base 5 number



for _ in [g, h]:
    if _ == g:
        fname = 'g'
    else:
        fname = 'h'
    of = open(f'{fname}.enc_test', 'wb')
    of.write(long_to_bytes(_))
    of.close()


of = open(f'g.enc', 'rb')

g = bytes_to_long(of.read())
of.close()

import string

def int_to_base(n, N):
    """ Return base N representation for int n. """
    base_n_digits = string.digits + string.ascii_lowercase + string.ascii_uppercase
    result = ""
    while n > 0:
        q, r = divmod(n, N)
        result += base_n_digits[r]
        n = q
    if result == "":
        result = "0"
    return "".join(reversed(result))

g = [int(i) for i in int_to_base(g, 5)]

for i in range(len(g) - c - 1, -1, -1):
    g[i] -= g[i+c]

g = g[c:]

f = g[:len(f)]
for i in range(len(f)-2, -1, -1):
    f[i] -= f[i+1]

print(f == f_final)
print(f)

bitstring = ''.join([str(i) for i in f])

f_num = int(bitstring, 2)

print(long_to_bytes(f_num))
