# For packets where reserved bit set, append 01 to each group of 2 packets' values
# (ip.src == 192.168.50.62)


vals = [
0b010,
0b010,

0b010,
0b011,

0b111,
0b011,

0b110,
0b010,

0b110,
0b011,

0b110,
0b110,

0b100,
0b010,

0b101,
0b001,

0b110,
0b100,

0b110,
0b011,

0b111,
0b101,
]

maybe = [
0b01010010,
0b01010011,
0b01111011,
0b01110010,
0b01110011,
0b01110110,
0b01100010,
0b01101001,
0b01110100,
0b01110011,
0b01111101,
]

print(''.join([chr(i) for i in maybe]))

# RS{rsvbits}
