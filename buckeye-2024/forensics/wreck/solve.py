# Found references to flag.jpg and jpeg data at this offset
with open('dump', 'rb') as f:
    f.seek(0x202D40)
    data = f.read(0x10000)

with open('flag.jpg', 'wb') as f:
    f.write(data)

# bctf{D4MN_7h47_c0r3_dvmp_907_4_GY477}
