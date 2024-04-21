import random
from pwn import *

#context.log_level = logging.DEBUG


MISS = b'\xe2\x96\xa1'
CONTAINS = b'\xe2\x97\xa9'
HIT = b'\xe2\x96\xa3'

BAD_CHARS = set([b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\x0e', b'\x0f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17', b'\x18', b'\x19', b'\x1a', b'\x1b', b' ', b'!', b'"', b'#', b'$', b'%', b'&', b"'", b'(', b')', b'*', b'+', b',', b'-', b'.', b'/', b':', b';', b'<', b'=', b'>', b'?', b'@', b'[', b'\\', b']', b'^', b'_', b'`', b'{', b'|', b'}', b'~', b'\x7f', b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x86', b'\x87', b'\x88', b'\x89', b'\x8a', b'\x8b', b'\x8c', b'\x8d', b'\x8e', b'\x8f', b'\x90', b'\x91', b'\x92', b'\x93', b'\x94', b'\x95', b'\x96', b'\x97', b'\x98', b'\x99', b'\x9a', b'\x9b', b'\x9c', b'\x9d', b'\x9e', b'\x9f', b'\xa0', b'\xa1', b'\xa2', b'\xa3', b'\xa4', b'\xa5', b'\xa6', b'\xa7', b'\xa8', b'\xa9', b'\xaa', b'\xab', b'\xac', b'\xad', b'\xae', b'\xaf', b'\xb0', b'\xb1', b'\xb2', b'\xb3', b'\xb4', b'\xb5', b'\xb6', b'\xb7', b'\xb8', b'\xb9', b'\xba', b'\xbb', b'\xbc', b'\xbd', b'\xbe', b'\xbf', b'\xc0', b'\xc1', b'\xc2', b'\xc3', b'\xc4', b'\xc5', b'\xc6', b'\xc7', b'\xc8', b'\xc9', b'\xca', b'\xcb', b'\xcc', b'\xcd', b'\xce', b'\xcf', b'\xd0', b'\xd1', b'\xd2', b'\xd3', b'\xd4', b'\xd5', b'\xd6', b'\xd7', b'\xd8', b'\xd9', b'\xda', b'\xdb', b'\xdc', b'\xdd', b'\xde', b'\xdf', b'\xe0', b'\xe1', b'\xe2', b'\xe3', b'\xe4', b'\xe5', b'\xe6', b'\xe7', b'\xe8', b'\xe9', b'\xea', b'\xeb', b'\xec', b'\xed', b'\xee', b'\xef', b'\xf0', b'\xf1', b'\xf2', b'\xf3', b'\xf4', b'\xf5', b'\xf6', b'\xf7', b'\xf8', b'\xf9', b'\xfa', b'\xfb', b'\xfc', b'\xfd', b'\xfe', b'\xff'])

wordlist = []
#with open('rockyou.txt', 'rb') as f:
#    wordlist = set()
#    for line in f.readlines():
#        line = line.strip()
#        skip = False
#        for c in line:
#            if bytes([c]) in BAD_CHARS:
#                skip = True
#                break
#        if skip:
#            continue
#        wordlist.add(line)
#    wordlist = list(wordlist)
#
#with open('rockyou_filtered.txt', 'wb') as f_out:
#    for i in wordlist:
#        f_out.write(i + b'\n')

#assert isinstance(wordlist[0], bytes)

#for i in range(256):
#    print(i)
#    r = remote('rockyoudle-1.play.hfsc.tf', 10000)
#    r.readuntil(b'lets play: ')
#    word_len = len(r.readline().strip().split(b' '))
#    r.sendline(chr(i)*word_len)
#    r.readline()
#    r.readline()
#    if b'incorrect chars' in r.readline():
#        BAD_CHARS.append(bytes([i]))
#    r.close()
#
#
#print(BAD_CHARS)
#exit(0)


with open('rockyou_filtered.txt', 'rb') as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        # omg it's case insensitive that explains so much
        wordlist.append(line.decode('charmap').lower())

#FREQ = defaultdict(int)
#for i in wordlist:
#    for c in set(i):
#        FREQ[c] += 1
#
#MOST_FREQ = [chr(i) for i in sorted(FREQ.keys(), key=lambda x: FREQ[x])][::-1]
#print(MOST_FREQ)

MOST_FREQ = ['a', 'e', '1', 'i', '2', 'n', '0', 'o', 'r', 'l', 's', '3', '9', 't', '8', '4', 'm', '5', '7', '6', 'c', 'd', 'y', 'h', 'u', 'k', 'b', 'g', 'p', 'j', 'v', 'f', 'w', 'z', 'A', 'x', 'E', 'I', 'R', 'L', 'N', 'S', 'O', 'M', 'T', 'C', 'D', 'q', 'B', 'H', 'Y', 'K', 'U', 'G', 'P', 'J', 'F', 'V', 'W', 'Z', 'X', 'Q']

r = remote('rockyoudle-1.play.hfsc.tf', 10000)

word_len = 0
round_num = 0
guess_num = 0
while True:
    pls: bytes = r.recv(timeout=0.5)

    for line in pls.splitlines():
        if b'lets play' in line:
            result = line.split(b': ')[1].strip().split(b' ')
            if word_len == 0:
                print("round", round_num)
                round_num += 1
                word_len = len(result)
                candidates = list(filter(lambda x: len(x) == word_len, wordlist))
            else:
                res_str = '  '
                for i,x in enumerate(result):
                    if x == HIT:
                        res_str += "1"
                    if x == CONTAINS:
                        res_str += "0"
                    if x == MISS:
                        res_str += "X"
                print(res_str)

                def does_match(cand: str):
                    for i in range(len(result)):
                        if result[i] == HIT and cand[i] != guess[i]:
                            return False
                        if result[i] == CONTAINS and (cand[i] == guess[i] or guess[i] not in cand):
                            return False
                        if result[i] == MISS and guess[i] in cand:
                            return False
                    return True

                candidates = list(filter(does_match, candidates))
                pass
        elif b'correct' in line:
            word_len = 0
            guess_num = 0
            print(line)
        elif b'game over' in line:
            print("We lost")
            exit(0)
        elif b'> ' in line:
            print("waiting for guess")
            print(len(candidates))
            if len(candidates) == 0:
                print("idk how we got here")
                r.interactive()
            guess = random.choice(candidates)
            print(guess)
            r.sendline(guess.encode('charmap'))
            guess_num += 1
            print("sent")
        elif b'midnight' in line:
            print(line)

# midnight{quend4ev3r4ndev3r}
