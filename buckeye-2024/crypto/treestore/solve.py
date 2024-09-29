"""
starting from the beginning of the file, store bytes, get how many new chunks were added, 0 new chunks means we found it

FLAG WILL CHANGE ON EVERY CONNECTION

need to generate images

can we send one incrementing chunk at the beginning to ensure we don't conflict with ourselves
"""

from base64 import b64encode
from pwn import remote, context
from PIL import Image, ImageFont, ImageDraw
import string

context.log_level = 'debug'

#HOST = 'challs.pwnoh.io'
#PORT = 13420

HOST = '127.0.0.1'
PORT = 1024
r = remote(HOST, PORT)


flag_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{_}"

# len(flag) < 32


def render(msg: str):
    char_size = (16, 32)  # (width, height)
    width = char_size[0] * len(msg)
    image = Image.new("RGBA", (width, char_size[1]), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load("./treestore/ter-x32b.pil")  # Terminus 32px
    draw.text((0, 0), msg, font=font)
    image.save("flag.bmp", format="BMP")


def store_data(data: bytes):
    r.sendlineafter(b'>>> ', b64encode(data))
    out = r.recvline()
    try:
        return int(out.split()[0])
    except Exception as e:
        print(e)
        print(out)

chunk_size = 16
num_flag_chunks = int(r.recvline().split()[0])

print(f'flag has {num_flag_chunks} chunks')

#for flag_len in range(5, 32):
#    render('_'*flag_len)
#    with open('flag.bmp', 'rb') as f:
#        flag_data = f.read()
#    num_added_chunks = store_data(flag_data[:16])
#    if num_added_chunks == 0:
#        break
#
#print(f'flag has {flag_len} chars')

flag_len = 31
guess = 'bctf'

if len(guess) < flag_len:
    guess += ' '*(flag_len - len(guess))

render(guess)
with open('flag.bmp', 'rb') as f:
    guess_data = f.read()
#num_added_chunks = store_data(flag_data[:16*5])

bytes_per_pixel = 4
image_width_px = len(guess) * 16
bitmap_data_start = 0x36 + 0xa
row_num = 6 # row to use to compare
bytes_per_row = image_width_px * bytes_per_pixel
row_data_start = bitmap_data_start + (bytes_per_row * row_num)



assert row_data_start % 16 == 0, hex(bytes_per_row)


row_bytes = guess_data[row_data_start:row_data_start + bytes_per_row]

#render(known_flag + 'a')
# TODO: choose a scanline across the image, and send that

print(store_data(row_bytes))

#r.interactive()
