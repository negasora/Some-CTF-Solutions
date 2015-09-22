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

```

Then, each of the keys that resulted in a valid header were saved to a file which was then processed by:

```python

```

This is where I got stuck. I could make the header anything I wanted with a given key, but I needed to guess the right file type.
I ended up barely missing out on the submission time with my working guess: PDF.
Using the PDF header, we got a key: BIZZ
and, upon decrypting with that key, we get

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
