Bricks of Gold

Crypto - 500

We've captured this encrypted file being smuggled into the country. All we know is that they rolled their own custom CBC mode algorithm - its probably terrible.
HINT: take a second look at the file for elements needed for the crypto


So, all you know about the file is that's it's encrypted with some kind of CBC algorithm, and that it's annoyingly large.

Basically the way that a CBC algorithm works for encryption is the plaintext is broken up in to blocks, and encryption/decrpytion is handled on a block-by-block basis.

The first block is XOR-d with an Initialization Vector(IV), and is then put through another (unknown in our case) encryption method, along with a key (also unknown in our case). The result is the first block of ciphertext.
This process is applied for all other blocks of plaintext, except instead of xor-ing with the IV, the most recently calculated block of ciphertext is used instead.

Finally, all these blocks are thrown together to create the glorious monstrosity of ciphertext we were given.

Decryption is basically the exact same thing, but reversed: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/CBC_decryption.svg/601px-CBC_decryption.svg.png

Looking at this (pre-hint), there was no clear indication for what the IV was, until I ran strings on it and "THE_SECRET_IV=CASH" was thrown at my face.
Okay, now we have the IV, but not the encryption method or key. They said the algorithm is probably terrible, and it's obviously reversible, so I assumed XOR.

The final step to complete decryption was finding the key. Asking around, I gathered that, when decrypted, it was a valid file; so therefore it has to have a valid header!

Knowing key length == IV length, I went to checking keys to find matching headers to some more popular filetypes:

```python
IV = "43 41 53 48".split(" ")
ctxt = "24 58 4D 54".split(" ")
head = "ff d8 ff e0".split(" ")

#jpeg = ff d8 ff e0
#png = 89 50 4e 47


def toByte(i):
	return hex(i)[2:]

for i in xrange(0,4):
	print toByte((int(ctxt[i], 16) ^ int(head[i], 16)) ^ int(IV[i], 16)).decode('hex')
```

Then, each of the keys that resulted in a valid header were saved to a file which was then processed by:

```python
import itertools, string, thread, magic
import os

def xor(s1, s2):
	out = ""
	if len(s1) == len(s2):
		out = ''.join(chr(ord(c)^ord(k)) for c,k in izip(s1, cycle(s2)))
	else:
		out = ''.join(chr(ord(c)^ord(k)) for c,k in izip(s1, cycle("\x00"+s2)))
		print "Different length strings"
	return out

import collections, operator
from itertools import cycle, izip
f = open("crypto500", "rb")
data = f.read()
f.close()

def dec(s, key):
	s = s.encode('hex')
	out = hex(int(s, 16) ^ int(key.encode('hex'),16))[2:]
	if not len(out)%2 == 0:
		out = "0" + out
	return out.decode('hex')

blocksize = 4 #4 bytes, 32 bit blocksize

hopeful = ""

def decrypt(key):	
	tempplain = []
	cipher = []
	counter = 0
	working = ""
	apptemp = tempplain.append
	appcip = cipher.append
	appcip(data[0:blocksize])

	working = data[0:blocksize]
	working = xor(working, key)

	tempplain.append(xor("CASH", working)) 

	for j in xrange(blocksize,len(data)-blocksize, blocksize):
		appcip(data[j:j+blocksize])
	
		working = data[j:j+blocksize]

		working = xor(data[j:j+blocksize], key)

		working = xor(cipher[counter], working)
	
		apptemp(working)
		counter = counter + 1

	f = open("out/try"+str(key), "wb")
	print len(''.join(tempplain))
	f.write(''.join(tempplain))
	f.close()

import sys

decrypt(sys.argv[1])

```

This is where I got stuck. I could make the header anything I wanted with a given key, but I needed to guess the right file type.
I ended up barely missing out on the submission time with my working guess: PDF.
Using the PDF header, we got a key: BIZZ
and, upon decrypting with that key, we get a PDF containing:

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
