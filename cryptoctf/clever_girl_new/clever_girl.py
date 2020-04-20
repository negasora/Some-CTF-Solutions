#!/usr/bin/env python

import gmpy2
from fractions import Fraction
#from secret import p, q, s, X, Y
#from flag import flag

#p = 168021530133679429891220120471761420849
#q = 168033629505992564641633634795516494631

#n = p*q
#s = n

import random, math

#s = random.randint((2*n + p + q + 1)/2, (p+1)*q)

# These must hold for X,Y to be positive
#assert 2*(p+1)*q > 2*s > 2*n + p + q + 1
#assert 2*s - 2*n - p - q - 1 > 0
#assert (p+1)*q - s > 0
#assert 2*s > 2*n + p + q + 1
#assert (p+1)*q > s
#assert q > p + 1


#X = 2*s - 2*n - p - q - 1
#Y = n + q - s
#print X
#print Y

#assert gmpy2.is_prime(p) * gmpy2.is_prime(q) > 0
#assert Fraction(p, p+1) + Fraction(q+1, q) == Fraction(2*s - X, s + Y)
#assert Fraction(p, p+1) + Fraction(q+1, q) == Fraction((p+1)*(q+1) + q*p, q*(p+1)) == Fraction(2*n + p + q + 1, n + q) == 1 + Fraction(n+p+1, n+q) == Fraction(2*(-n) - -1*(4*n + p + q + 1), -n + 2*n + q)


# print 'Fraction(p, p+1) + Fraction(q+1, q) = Fraction(2*s - {X}, s + {Y})'.format(X=X, Y=Y)


# X + 2Y = 2*s - 2*n - p - q - 1 + 2*n + 2*q - 2*s = q - p - 1
#print X + 2*Y
#print q - p - 1

from sage.all import *

X = 153801856029563198525204130558738800846256680799373350925981555360388985602786501362501554433635610131437376183630577217917787342621398264625389914280509
Y = 8086061902465799210233863613232941060876437002894022994953293934963170056653232109405937694010696299303888742108631749969054117542816358078039478109426
n = 161010103536746712075112156042553283066813155993777943981946663919051986586388748662616958741697621238654724628406094469789970509959159343108847331259823125490271091357244742345403096394500947202321339572876147277506789731024810289354756781901338337411136794489136638411531539112369520980466458615878975406339
c = 64166146958225113130966383399465462600516627646827654061505253681784027524205938322376396685421354659091159523153346321216052274404398431369574383580893610370389016662302880230566394277969479472339696624461863666891731292801506958051383432113998695237733732222591191217365300789670291769876292466495287189494

q = var('q')


a = 1
b = -(2*Y + X - 1)
c = -n


#d = sqrt(b*b - 4*c)
#q = (d+b)/2
#p = n/q
#e = 0x10001
#d = 1/e % lcm(p-1,q-1)
#m2 = pow(ct,d,n)

poly = (q**2) + b*q + c
roots = poly.roots()

q = (-b + sqrt((b*b) - (4*c)))/2
p = n/q

print q


e = 0x10001
d = 1/e % lcm(p-1,q-1)
m2 = pow(ct,d,n)

mp = mod(m2,p).sqrt()
mq = mod(m2,q).sqrt()

m = crt([int(mp),int(mq)],[p,q])
print m.hex().decode('hex')

#flag = "hi this is flag"
#c = pow(int(flag.encode('hex'), 16), 0x20002, n)
#print 'n =', n
#print 'c =', c
