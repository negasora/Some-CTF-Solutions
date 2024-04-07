with open('emails/email5.enc', 'rb') as f:
    ctxt = f.read()

print(len(ctxt)%32)


last_bytes= b"hanks,\x0d\x0a- Your Secret Conspirato"

assert len(last_bytes) == 32

key = [c ^ last_bytes[i] for i,c in enumerate(ctxt[-33:-1])]


print(key)


ptxt = ''
for i,c in enumerate(ctxt):
    ptxt += chr(c ^ key[i % len(key)])

print(ptxt)

# RS{Th4T's_n0T_h0w_Y0u_u53_OTP}
