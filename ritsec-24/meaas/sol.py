import binascii
from math import lcm

from string import printable

n = 1970384981
c1 = 184323288
c2 = 306942680
c3 = 1791553791
# API Key: abadbd796f1b2ae8bd82e1195ad12373


# I just factored it :|
p = 34913
q = 56437
phi = lcm(p-1, q-1)

assert p*q == n

count = 0
for e in range(1, 65536):
    try:
        d = pow(e, -1, phi)
    except:
        continue

    ptxt = ''
    for ctxt in [c1, c2, c3]:
        p = hex(pow(ctxt, d, n))[2:]
        if len(p) % 2 == 1:
            p = '0' + p
        ptxt += binascii.unhexlify(p).decode('charmap')

    if all(i in printable for i in ptxt):
        print(ptxt)
    count += 1

# RC{b3etr007}
