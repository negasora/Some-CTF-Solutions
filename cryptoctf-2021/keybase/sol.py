from pwn import *

from Crypto.Util import number
from Crypto.Cipher import AES
import binascii
ptxt = "\x00"*32
ptxt_bytes = ptxt.encode('charmap')
#r = process(['python', './keybase.py'])
r = remote('01.cr.yp.toc.tf', 17010)
while True:
    r.sendlineafter('[Q]uit', 't')

    r.sendlineafter('to encrypt:', ptxt)
    r.readuntil('enc = ')
    enc = r.readline().strip().decode('charmap')
    r.readuntil('key = ')
    key_known = bytes.fromhex(r.readline().strip()[:-4].decode('charmap'))

    if enc.index('*') == 4:
        break
    print("bad enc,", enc.index('*'))
print('got good enc')
known_enc_begin = bytes.fromhex(enc[:enc.index('*')])
enc_blocks = [enc[i:i+32] for i in range(0, len(enc), 32)]
last_block = bytes.fromhex(enc_blocks[-1])
print(last_block)
print(enc)

def check_enc(out):
    for i in range(32):
        if enc[i] == '*':
            continue
        if enc[i] != out[i]:
            return False

# use null ptxt to avoid xor
# brute key last 2 bytes
# try decrypting last block to get enc(iv^ptxt)
# check that that block beginning matches what we're given to speed up guessing
# decrypt enc(iv^ptxt) for iv yay null ptxt
# try decrypt with key guess and iv guess


def decrypt(enc, iv, key):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(enc)


def get_flag(iv, key):
    r.sendlineafter('[Q]uit', 'g')
    r.readuntil('flag) = ')
    enc_flag = r.readline().strip()
    out = decrypt(binascii.unhexlify(enc_flag), iv, key).decode('charmap')
    print(out)

empty_iv = b'\x00'*16
for x in range(256):
    for y in range(256):
        key_guess = key_known + bytes([x, y])
        enc_iv = decrypt(last_block, empty_iv, key_guess)
        if enc_iv[:2] != known_enc_begin:
            continue
        aes = AES.new(key_guess, AES.MODE_ECB)
        dec_iv = aes.decrypt(enc_iv)
        get_flag(dec_iv, key_guess)



