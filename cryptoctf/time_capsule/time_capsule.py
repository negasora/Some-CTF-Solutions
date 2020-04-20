#!/usr/bin/python

from Crypto.Util.number import *
#from secret import flag, n, t, z

from sage.all import *
from ast import literal_eval
import requests, json

def encrypt_time_capsule(msg, n, t, z):
	m = bytes_to_long(msg)
	l = pow(2, pow(2, t), n)
	c = l ^ z ^ m
	return (c, n, t, z) 


c,n,t,z = literal_eval(open('time_capsule.txt','rb').read().strip())

r = requests.get("http://factordb.com/api?query={}".format(n))
facs = json.loads(r.text)['factors']

factors = []
for f in facs:
    for i in range(int(f[1])):
        factors.append(int(f[0]))

tot_phi = 1

for f in factors:
    tot_phi *= euler_phi(f)

l = pow(2, pow(2, t, int(tot_phi)), n)
m = int(l) ^ int(z) ^ int(c)

print(hex(m)[2:-1].decode('hex'))
