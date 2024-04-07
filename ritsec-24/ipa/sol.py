with open('challenge.txt') as f:
    data = []
    for i in f.readlines():
        data += i.strip().split()
print(data)



chars = {
    '0020': ('\u0020', ''),
    '0064': ('\u0064', 'd'),
    '0065': ('\u0065', 'e'),
    '0066': ('\u0066', 'f'),
    '0069': ('\u0069', 'i'),
    '0073': ('\u0073', 's'),
    '0074': ('\u0074', 't'),
    '026a': ('\u026a', 'I'),
    '0292': ('\u0292', '3'),
    '02b2': ('\u02b2', 'j'),
    '02c8': ('\u02c8', '\''),
    '02d0': ('\u02d0', ':'),
    '0361': ('\u0361', 'n'),
}

print(chars)

import binascii


data = [chars[i][1] for i in data]

with open('out', 'w') as f:
    f.write(''.join(data))
