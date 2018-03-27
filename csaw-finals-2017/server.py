from pwn import *

p = 251
g = 6
b = 17


def encdec(s):
	global ss
	out = ""
	for i in s:
		out += chr(ord(i) ^ ss)
	return out


while True:
	r = listen(31337)


	_ = r.wait_for_connection()

	A = ord(r.recv(1))

	ss = pow(A, b, p)
	B = pow(g, b, p)

	r.send(chr(B))
	print encdec(r.read())
	r.send(encdec("P\xff\xff\xff\xff\r\nT\tHi,KEY\r\nC\tKEY:FLAG\r\nF\t/client/py\tnegasora.com\t31337"))
	#r.send(encdec("P\xff\xff\xff\xff\r\nT\tHi,KEY\r\nC\tKEY:FLAG\r\nL\t/client/py\tnegasora.com\t31337"))
	r.close()
	
	r = listen(31337)


	_ = r.wait_for_connection()

	A = ord(r.recv(1))

	ss = pow(A, b, p)
	B = pow(g, b, p)

	r.send(chr(B))
	print encdec(r.read())
	r.send(encdec("IDEA\r\nimport os\r\nos.system('cat /flag.txt')"))
	r.close()
