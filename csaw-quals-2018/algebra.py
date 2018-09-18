from pwn import *
from sage.all import *
import re



while True:
    r = remote("misc.chal.csaw.io", 9002)

    r.read()

    try:
        while True:
            X = var("X")
            asd = r.read()
            if "flag" in asd:
                print asd
                exit(0)
            print asd.split("\n")
            eq = [eval(asd.split("\n")[0].replace("=", "=="))]
            #print eq
            sol = str(solve(eq, X)[0]).split("== ")[1]
            print eval(sol)
            #print sol
            sol = str(eval(str(sol.replace("/",".0/"))))
            if re.match(r"-?[0-9]+ == -?[0-9]+", str(sol)):
                r.interactive()
            r.sendline(sol)
            print r.readline()
    except Exception as e:
        continue
