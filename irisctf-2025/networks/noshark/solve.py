import binascii

packet_num = 0
with open('noshark.txt', 'r') as f:
    data = b''
    for line in f.readlines()[3:]:
        if len(line) < 132:
            continue
        line = line.strip()[132:]
        data += binascii.unhexlify(line)
    with open('image.jpeg', 'wb') as outf:
        outf.write(data)

# irisctf{welcome_to_net_its_still_ez_to_read_caps_without_wireshark}
