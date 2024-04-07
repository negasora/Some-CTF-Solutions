from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa


ctxts = []
keys: list[rsa.RSAPublicNumbers] = []

for i in range(1,4):
    with open(f'file{i}.txt', 'rb') as f:
        ctxts.append(int(f.read().hex(), 16))

    with open(f'pk{i}.pem', 'rb') as f:
        key: rsa.RSAPublicKey = load_pem_public_key(f.read()) # type: ignore
        keys.append(key.public_numbers())


def eegcd(a, b):
    # Base Case
    if a == 0 :
        return b,0,1

    gcd,x1,y1 = eegcd(b%a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y


from math import gcd


for i,ictxt in zip(keys, ctxts):
    for j,jctxt in zip(keys, ctxts):
        if i.n == j.n and i.e == j.e:
            continue
        if gcd(i.n, j.n) == 1:
            continue

        _,a,b = eegcd(i.e, j.e)


        if a < 0:
            pos = b
            neg = a
        else:
            pos = a
            neg = b

        a = pos
        b = neg

        inv = pow(jctxt, -1, j.n)

        ptxt = (pow(ictxt, a, i.n) * pow(inv, -b, i.n)) % i.n

        print(bytes.fromhex(hex(ptxt)[2:]))

# p**e1 % n = c1
# p**e2 % n = c2


# RS{Y0U_C4NT_R3AD_M3_R1GHT??}
