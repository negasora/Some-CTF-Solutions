# missing 2nd half of ctxt :P

from hashlib import sha256
import base64

key_init = bytes.fromhex(sha256(b'Getting warmer').hexdigest())
key_xor = bytes.fromhex('c6dce591db79299802e84c22455a1eab040d59f8eafedbf332ddf2b7fafaaea8')
ctxt = base64.b64decode("uvn3YwgzZ4RVT4xRulclxzGgUGAtKEPOxW/yP3mOwMa7nQ+Q260G+08raB0XSPX7")
ctxt += bytes.fromhex('692bbc41b29c7832eb8b074a089ba8fbfb360032b276683c40d2ecdbb49b822bf5261fb39adc454e14c82a763970a8f1')

key = b''
for i,j in zip(key_init, key_xor):
    key += chr(i^j).encode('charmap')

print(len(key_init))
iv = bytes.fromhex("88150bfc7a8245dcccbc7b2942535df6")


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
print(decryptor.update(ctxt) + decryptor.finalize())



'The first half of the cipher text is uvn3YwgzZ4RVT4xRulclxzGgUGAtKEPOxW/yP3mOwMa7nQ+Q260G+08raB0XSPX7'
'The key must be XORed with 0b1100011011011100111001011001000111011011011110010010100110011000000000101110100001001100001000100100010101011010000111101010101100000100000011010101100111111000111010101111111011011011111100110011001011011101111100101011011111111010111110101010111010101000 in order to work'
'The iv is 180775230571011695939483724432608877824, more or less'
'The key is a sha256 hash of "Getting warmer", though that doesn\'t work by itself. The cipher is AES CBC.'
'The missing bytes in the iv are [21, 252, 130, 220, 188, 41, 83, 246]'
'The second half of the cipher text is 692bbc41b29c7832eb8b074a089ba8fbfb360032b276683c40d2ecdbb49b822bf5261fb39adc454e14c82a763970a8f1'


# RS{Michael_stole_the_invention}
