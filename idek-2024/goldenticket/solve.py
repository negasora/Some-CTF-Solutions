flag = 1234
p = 65537

A = (pow(13, flag-1, p) + pow(37, flag-1, p))%p
B = (pow(13, flag, p) + pow(37, flag, p))%p

pls = (B*pow(A, -1, p))%p
print(A)
print(B)
print(pls)
