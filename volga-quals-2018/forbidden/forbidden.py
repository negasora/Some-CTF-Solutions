from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
#from secret import key
from pwn import *


def encrypt(iv, key, plaintext, associated_data):
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    

    encryptor.authenticate_additional_data(associated_data)
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (ciphertext, encryptor.tag)


def decrypt(key, associated_data, iv, ciphertext, tag):
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    decryptor.authenticate_additional_data(associated_data)

    return decryptor.update(ciphertext) + decryptor.finalize()


iv = "9313225df88406e555909c5aff5269aa".decode('hex')
#key = key.decode('hex')


(A1, C1, T1) = ("John Doe".encode("hex"), "1761e540522379aab5ef05eabc98516fa47ae0c586026e9955fd551fe5b6ec37e636d9fd389285f3", "0674d6e42069a10f18375fc8876aa04d")
(A2, C2, T2) = ("VolgaCTF".encode('hex'), "1761e540522365aab1e644ed87bb516fa47ae0d9860667d852c6761fe5b6ec37e637c7fc389285f3", "cf61b77c044a8fb1566352bd5dd2f69f")
(A3, C3) = ("John Doe".encode('hex'), "1761e540522379aab5ef05eabc98516fa47ae0d9860667d852c6761fe5b6ec37e646a581389285f3")


# tools from https://github.com/nonce-disrespect/nonce-disrespect
p = process(["./tool/recover", A1, C1, T1, A2, C2, T2], level="ERROR")

maybe_hash_key = p.readall().strip().split("\n")

for idk in maybe_hash_key:
    p = process(["./tool/forge", A1, C1, T1, A3, C3, idk], level="ERROR")
    for line in p.readall().strip().split("\n"):
        print "flag might be: VolgaCTF{" + line + "}"


#ciphertext1, tag1 = encrypt(iv, key, "From: John Doe\nTo: John Doe\nSend 100 BTC", "John Doe")
#ciphertext2, tag2 = encrypt(iv, key, "From: VolgaCTF\nTo: VolgaCTF\nSend 0.1 BTC", "VolgaCTF")
#ciphertext3, tag3 = encrypt(iv, key, "From: John Doe\nTo: VolgaCTF\nSend ALL BTC", "John Doe")

