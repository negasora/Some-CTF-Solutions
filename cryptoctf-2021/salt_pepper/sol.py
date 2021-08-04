#from hashpumpy import hashpump
#import hashlib
#
#import hashpumpy
#key           =  b'A'*19
#
#import hashlib
#
#md5_prefix = '5f72c4360a2287bc269e0ccba6fc24ba'
#sha1_prefix = '3e0d000a4b0bd712999d730bc331f400221008e0'
#
##md5_prefix = hashlib.md5(key).hexdigest()
##sha1_prefix = hashlib.sha1(key).hexdigest()
#
#
#md5_new_digest, md5_new_data = hashpumpy.hashpump(md5_prefix, '', 'n3T4Dm1n', len(key))
#
#sha1_new_digest, sha1_new_data = hashpumpy.hashpump(sha1_prefix, '', 'P4s5W0rd' + md5_new_digest, len(key))
#
#print(md5_new_data)
#print(sha1_new_data)
#print(sha1_new_digest)


#print(md5_new_data)
#print(md5_new_digest)
#print(sha1_new_data[:-len(md5_new_digest)])
#print(sha1_new_digest)

from pwn import *

username = b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x98\x00\x00\x00\x00\x00\x00\x00n3T4Dm1n'
password = b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x98P4s5W0rd'
new_hash = '83875efbe020ced3e2c5ecc908edc98481eba47f'
r = remote("02.cr.yp.toc.tf", 28010)
r.sendlineafter('[Q]uit', 'l')

r.sendlineafter('comma:', username.hex()+','+password.hex())
r.sendlineafter('hash:', new_hash)
r.interactive()
