#!/usr/bin/env python

from Crypto.Util.number import *
#from secret import exp, flag, nbit
from sage.all import *
flag = 12345
exp = 255
nbit = 128

assert exp & (exp + 1) == 0
# exp = pow(2,x) - 1 or 0

def adlit(x): # invert bits
    l = len(bin(x)[2:])
    return (2 ** l - 1) ^ x

def genadlit(nbit):
    while True:
        p = getPrime(nbit)
        q = adlit(p) + 31337
        if isPrime(q):
            return p, q

p, q = genadlit(nbit)
e, n = exp, p * q

c = pow(flag, e, n)
print bin(p)
def aaa(x, l): # invert bits
    return (2 ** l - 1) ^ x
print bin(q)
nbit = len(bin(n))/2
print bin(aaa(q, nbit))
print inverse_mod(n, c)
print bin(p)
print bin(q)

print 'n =', n
print 'c =', c

