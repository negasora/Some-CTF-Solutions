import binascii
import subprocess

with open('known_plaintext', 'wb') as f:
    f.write(binascii.unhexlify("89504e470d0a1a0a0000000d494844520000"))


subprocess.run(
    [
        'bkcrack',
        '-C',
        'dogs_wearing_tools.zip',
        '-c',
        '1.png',
        '-p',
        'known_plaintext'
    ],
    check=True
)

"""
[01:05:18] Keys
adf73413 6f6130e7 0cfbc537
"""


subprocess.run(
    [
        'bkcrack',
        '-k',
        'adf73413',
        '6f6130e7',
        '0cfbc537',
        '--bruteforce',
        '?a',
        '--length',
        '12'
    ],
    check=True
)

# Password: 2n3Ad3&ZxDvV

