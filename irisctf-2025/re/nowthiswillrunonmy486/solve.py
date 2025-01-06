

print((0xbf51b0d7^0xcc38c2be).to_bytes(4, 'little'))



pairs = [
    (0xcc38c2be, 0xbf51b0d7),
    (0xeaa2018, 0x75cc547b ),
    (0x1078b74d, 0x4f0fd83a),
    (0xdb631232, 0xa2117744),
    (0x98a0a199, 0xecd0cec6),
    (0x42789493, 0x2e19f9fa),
    (0x5685e086, 0x32ea83d9),
    (0x98ca4085, 0xe5eb61e0),
]

flag = b''.join((i[0]^i[1]).to_bytes(4, 'little') for i in pairs)

print(flag)
