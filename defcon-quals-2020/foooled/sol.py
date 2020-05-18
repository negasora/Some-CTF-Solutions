from sage.all import *

from pwn import remote, process

# https://www.math.leidenuniv.nl/scripties/Broker.pdf page 18
def gen_curve_naive(min_p):
    # doesn't work rn, probably misunderstood notation
    N = min_p
    # 1
    a = N + 1 - (N.nth_root(2, truncate_mode=1)[0].ceil())
    while True:
        #1a
        if a > N + 1 + sqrt(N):
            print("FAILURE at ")
            exit(1)
        #1b
        if a.is_prime():
            p = a
            t = p + 1 - N
            break
        else:
            a = a + 1
    print("GOT A")
    print(a)

    # 2
    while True:
        b = GF(p).random_element()
        # we ignore removing 0 and -27*inv(4) (if that's what the notation means) since there's a small chance of those being chosen
        print(b)
        #2a
        Eb = EllipticCurve([b, -b])
        P = Eb(1, 1) # iffy on this syntax in the paper, might be over GF(p)?
        print(P)
        #2b
        if (p + 1 - t)*P == Eb.order(): # might not be order
            print("FIRST CONDITION")
            u = Eb.trace_of_frobenius()
            if u == t:
                return Eb
        #2c
        if t != 0 and (p + 1 + t)*P == Eb.order(): # might not be order
            print("SECOND CONDITION")
            u = Eb.trace_of_frobenius()
            if u == -t:
                return Eb.quadratic_twist()

# hey someone do this
def gen_curve_efficient(min_p):
    pass



#r = remote("notbefoooled.challenges.ooo", 5000)
r = process(["sage", "service.sage"])

r.readuntil("greater than ")

min_p = Integer(r.readuntil(":")[:-1])
print(min_p)
print(is_prime(min_p))

coeffs, p = gen_curve_efficient(min_p)

r.sendlineafter("a =", str(coeffs[0]))
r.sendlineafter("b =", str(coeffs[1]))
r.sendlineafter("p =", str(p))

r.interactive()
