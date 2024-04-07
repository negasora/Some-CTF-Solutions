# Tried a sol from github, didn't work

import binascii

import json

with open('output.json', 'rb') as f:
    data = json.load(f)
    ct = int.from_bytes(binascii.unhexlify(data['enc_key']))
    public_key = data['pub_key']

# open the public key and strip the spaces so we have a decent array
nbit = len(public_key)
# open the encoded message
encoded = ct
print("start")
# create a large matrix of 0's (dimensions are public key length + 1)
A = Matrix(ZZ,nbit+1,nbit+1)
# fill in the identity matrix
for i in range(nbit):
    A[i,i] = 1
# replace the bottom row with your public key
for i in range(nbit):
    A[i,nbit] = public_key[i]
# last element is the encoded message
A[nbit,nbit] = -int(encoded)

res = A.LLL()

for i in range(0, nbit + 1):
    # print solution
    M = res.row(i).list()
    flag = True
    for m in M:
        if m != 0 and m != 1:
            flag = False
            break
    if flag:
        M = ''.join(str(j) for j in M)
        # remove the last bit
        M = M[:-1]
        M = int('0b'+M,2)
        print(M)

