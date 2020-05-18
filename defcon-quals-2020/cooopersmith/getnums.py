from sage.all import *
from pwn import context, process, gdb, remote
context.terminal = ["xterm", "-e"]
from Crypto.PublicKey import RSA

import subprocess


#r = process('./service_patched_flag')
r = remote("coooppersmith.challenges.ooo", 5000)
#r = gdb.debug('./service_patched_flag', '''
#breakrva 0x1d19
#breakrva 0x1d32
#c
#''')


prefix = random_prime(2**51)
prefix_hex = hex(prefix).replace('0x', '').rjust(120, '0')
print(prefix_hex)
#r.sendline(hex(prefix)[2:])
r.sendline(prefix_hex)

r.readuntil("Your public key:\n")
key_b64 = r.readuntil("-----END RSA PUBLIC KEY-----")
k = RSA.importKey(key_b64)
print(k.e)
print(k.n)
r.readuntil("Question: \n")
#question = r.read().strip()
#print(question)
#q = int(question, 16)
question = r.readline().strip()

print("question:", question)

# this is bc I'm too lazy to do c int arith in python :D (also has hard coded offset bc server latency)
ans = subprocess.run("./rand_res_remote", capture_output=True).stdout.strip().decode()
print(ans)
r.sendline(ans)


r.readuntil("Your flag message:\n")

flag_msg = r.readline().strip()
print("flag msg:", flag_msg)
if len(flag_msg) == 0:
    print("prefix too small of prime (maybe just unlucky, try again)")
    exit(1)
flag_int = int(flag_msg, 16)

print(f"factor me: {k.n}")
print(f"ctxt flag as int: {flag_int}")


r.close()
