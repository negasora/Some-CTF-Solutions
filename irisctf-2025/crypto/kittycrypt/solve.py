to_replace = (
    ('0', "🐱"), ('1', "🐈"), ('2', "😸"), ('3', "😹"),
    ('4', "😺"), ('5', "😻"), ('6', "😼"), ('7', "😽"),
    ('8', "😾"), ('9', "😿"), ('A', "🙀"), ('B', "🐱‍👤"),
    ('C', "🐱‍🏍"), ('D', "🐱‍💻"), ('E', "🐱‍👓"), ('F', "🐱‍🚀"),
)[::-1]


with open('example_output.txt.real', 'r') as f:
    ctxt = f.read()

for i in to_replace:
    ctxt = ctxt.replace(i[1], i[0])


print(ctxt)

import binascii
import json
ctxt = binascii.unhexlify(ctxt).decode('utf8')
print(ctxt)

with open('example_input.txt.real', 'r') as f:
    ptxt = f.read()

recovered_keys = []
for i in zip(ptxt, ctxt):
    print(ord(i[1]))
    recovered_keys.append(ord(i[1]) - ord(i[0]))

with open('keys_46.json', 'r') as f:
    keys = json.loads(f.read())


print(keys)
print(recovered_keys)
#assert keys == recovered_keys



with open('flag_output.txt', 'r') as f:
    flag_ctxt = f.read()

for i in to_replace:
    flag_ctxt = flag_ctxt.replace(i[1], i[0])
flag_ctxt = binascii.unhexlify(flag_ctxt).decode('utf8')


a = ""
for i in range(len(flag_ctxt)):
    a += chr(ord(flag_ctxt[i]) - recovered_keys[i])
print(a)



