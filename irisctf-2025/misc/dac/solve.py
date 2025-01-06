from PIL import Image

im = Image.open('chal.png')

height_step = 7

start_y = 978
start_x = 0

# last row isn't complete so only include 0 or 1
end_x = im.width-1
end_y = 2838 # last row is at 2833


ZERO = (255, 255, 255, 255)
ONE = (0, 0, 0, 255)

def get_bits():
    bits = ""
    for y in range(start_y, end_y, height_step):
        for x in range(start_x, end_x):
            p = im.getpixel((x, y))
            if p == ONE:
                bits += '1'
            elif p == ZERO:
                bits += '0'
            else:
                print(f'invalid at {(x,y)}. exiting.')
                return bits
    return bits

import binascii

with open('out.wav', 'wb') as f:
    f.write(binascii.unhexlify(hex(int(get_bits(), 2))[2:]))

# idk what now probably multimon it
