"""
13^(x-1) + 37^(x-1) == A mod p
13^x + 37^x == B mod p

13_i = pow(13, -1, p)
37_i = pow(37, -1, p)

13_i*(13^x) + 37_i*(37^x) == A mod p

13^x = 13*(A - 37_i*(37^x)) mod p

13*(A - 37_i*(37^x)) + 37^x == B mod p
13A - 13*37_i*(37^x)+37^x == B mod p

13A - B == (37^x)*(13*37_i - 1) mod p

(13A - B)*pow(13*37_i - 1, -1, p) == 37^x mod p

left is known, solve discrete log
"""


# This file was *autogenerated* from the file sol.sage
from sage.all_cmdline import *   # import sage library

_sage_const_396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807 = Integer(396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807); _sage_const_88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247 = Integer(88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247); _sage_const_67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242 = Integer(67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_13 = Integer(13); _sage_const_37 = Integer(37); _sage_const_2 = Integer(2)


x = var('x')
p = _sage_const_396430433566694153228963024068183195900644000015629930982017434859080008533624204265038366113052353086248115602503012179807206251960510130759852727353283868788493357310003786807 

last_two = [_sage_const_88952575866827947965983024351948428571644045481852955585307229868427303211803239917835211249629755846575548754617810635567272526061976590304647326424871380247801316189016325247 , _sage_const_67077340815509559968966395605991498895734870241569147039932716484176494534953008553337442440573747593113271897771706973941604973691227887232994456813209749283078720189994152242 ]
A = last_two[_sage_const_0 ]
B = last_two[_sage_const_1 ]


left = (_sage_const_13 *A - B) % p

print(left)

cons = ((_sage_const_13 *pow(_sage_const_37 , -_sage_const_1 , p)) - _sage_const_1 ) % p
print(cons)

to_mul = pow(cons, -_sage_const_1 , p)
print(to_mul)

solve_for_me = (left * to_mul)%p
print(solve_for_me)

x = discrete_log(solve_for_me, Mod(_sage_const_37 , p))
print(bytes.fromhex(hex(x)[_sage_const_2 :]))



