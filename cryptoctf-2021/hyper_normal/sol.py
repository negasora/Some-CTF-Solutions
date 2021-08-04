#!/usr/bin/env python3

import random
#from flag import FLAG

# real flag is 55 chars long, makes list lengths match
FLAG = "A"*55

p = 8443

def transpose(x):
    result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    return result

def vsum(u, v):
    assert len(u) == len(v)
    l, w = len(u), []
    for i in range(l):
        w += [(u[i] + v[i]) % p]
    return w

def sprod(a, u):
    w = []
    for i in range(len(u)):
        w += [a*u[i] % p]
    return w


W_final = None
def encrypt(msg):
    global W_final
    l = len(msg) # 55
    hyper = [ord(m)*(i+1) for (m, i) in zip(list(msg), range(l))] # ord('f')*1, ord('l')*2, etc...

    V, W = [], []
    for i in range(l):
        v = [0]*i + [hyper[i]] + [0]*(l - i - 1)
        V.append(v)
    # puts char at flag index i in to a 2d list x at x[i][i]

    random.shuffle(V)
    print(V)

    for _ in range(l):
        R = [random.randint(0, 126) for _ in range(l)]
        v = [0]*l
        for j in range(l):
            temp = sprod(R[j], V[j]) # multiply list by random int
            print(temp)
            v = vsum(v, temp) # adds lists
            print(v)
        W.append(v)
    print(W)
    random.shuffle(transpose(W)) # random shuffle doesn't do anything...
    return W

enc = encrypt(FLAG)
#print(enc)

import json

enc_flag = json.loads(open('output.txt', 'r').read())
#enc_flag = enc.copy()


out = [[] for i in range(len(enc_flag))]

for i in enc_flag:
    for j in range(len(i)):
        out[j].append(i[j])
#print(enc_flag)

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

for i in range(len(enc_flag)):
    for j in range(len(enc_flag[i])):
        enc_flag[i][j] = (enc_flag[i][j] * modinv(j+1, p))%p


# we have each letter multiplied by random numbers

# gcd all members at index n???

#[[letter1*rand1, letter2*rand2, ..., lettern*randn], [letter1*(randn+1), letter2*(randn+2)), ...], ...]

from math import gcd




final_flag = ""
for index in range(len(enc_flag)):
    maybe = []
    good = False
    for b in range(len(enc_flag)):
        for i in range(len(enc_flag)):
            if i == b:
                continue
            out = gcd(enc_flag[b][index], enc_flag[i][index])
            if 0x20 <= out < 0x7f:
                maybe.append(chr(out))

    final_flag += max(set(maybe), key = maybe.count)
print(final_flag)

# (a**2)*(random1*random2)
