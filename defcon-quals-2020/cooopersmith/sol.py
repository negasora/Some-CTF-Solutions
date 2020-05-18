from sage.all import *
from binascii import unhexlify

# numbers from wilson's beast cpu

p = 35277863960339577657189972105136254573571659462893
q = 43125956343311539474842844676995575321534228145759

c = 0x0247969523cb0a593680949b0ef8a8986b07d4ddfc9aa91228c64cf4e23783a3fe6fc04dc0e00ee06a08


n = p*q
e = 65537

d = inverse_mod(e, (p-1)*(q-1))

flag = f"{int(pow(c, d, n)):x}"

if len(flag) % 2:
    flag = '0'+flag

print(unhexlify(flag))
