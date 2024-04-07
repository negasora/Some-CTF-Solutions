from pwn import *

r = remote('ctf.ritsec.club', 30148)







FLAG = "XD{THISS_IS_SHORT_TEST_FLAG}PADD"
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = secrets.token_bytes(16)
iv = secrets.token_bytes(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

REMOTE = True

def enc(msg: bytes):
    print(msg)
    if REMOTE:
        r.readuntil(b'Option >')
        r.sendline(b'1')
        r.readuntil(b' > ')
        r.sendline(msg)
        if b'error' in r.readuntil(b'Option >'):
            print("ERROR")
            print(msg)
            exit(1)
        r.sendline(b'3')
        r.readuntil(b'server: ')
        res = r.readline().strip()
        return res
    else:
        msg = msg.decode().format(FLAG).encode()
        encryptor = cipher.encryptor()
        ct = encryptor.update(msg) + encryptor.finalize()
        return(ct.hex())

import string

# flag is 28 bytes

alpha = string.digits + string.ascii_letters + string.punctuation

known = b''
while True:
    try:
        for i in range(len(known.decode().format('')), 32):
            block_num = (i//16)
            offset = (16)*(block_num + 1) - 1
            target = enc(b'A'*(offset - i) + b'{}' + b'A'*(i+1))
            for c in alpha:
                c = c.encode()
                if c == b'{':
                    c = b'{{'
                if c == b'}':
                    c = b'}}'
                res = enc(b'A'*(offset - i) + known + c + b'{}')
                print("TARGET", target)
                print("RESULT", res)
                if res[(block_num*32):((block_num+1)*32)] == target[(block_num*32):((block_num+1)*32)]:
                    known += c
                    print(known)
                    break
                if c.decode() == alpha[-1]:
                    print("fail :(")
                    exit(1)

    except EOFError:
        r = remote('ctf.ritsec.club', 30148)
        continue


# RS{0n3_Ch4r4cT3R_@t_4_t1Me}
