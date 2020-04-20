a = "D: mb xwhvxw mlnX 4X6AhPLAR4eupSRJ6FLt8AgE6JsLdBRxq57L8IeMyBRHp6IGsmgFIB5E :ztey xam lb lbaH"
print a[::-1]

# Habl bl max yetz: E5BIFgmsGI6pHRByMeI8L75qxRBdLsJ6EgA8tLF6JRSpue4RALPhA6X4 Xnlm wxvhwx bm :D 


subs = {
'H': 'T',
'a': 'h',
'b': 'i',
'l': 's',
'm': 't',
'x': 'e',
'y': 'f',
'e': 'l',
't': 'a',
'z': 'g',
'w': 'd',
'v': 'c',
'h': 'o',
'X': 'J',
'n': 'u'
        }


for i in subs:
    print i, subs[i], ord(i) - ord(subs[i])

out = ""
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
digits = "0123456789"
for c in a[::-1]:
    if c in lower:
        out += lower[(lower.index(c) + 7) % len(lower)]
    elif c in upper:
        out += upper[(upper.index(c) +12) % len(upper)]
    elif c in digits:
        out += digits[(digits.index(c) +5) % len(digits)]
    else:
        out += c
print out

encflag = out.split(': ')[1].split()[0]
print encflag.decode('base64')
