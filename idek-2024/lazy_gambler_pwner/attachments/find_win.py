import binaryninja as bn
import json

bv = bn.load('code.bin')

win_syms = ['execve', 'system', 'gets', 'fgets']
avoid_syms = []

win_addrs = []
avoid_addrs = []


for win_sym in win_syms:
    s = bv.get_symbol_by_raw_name(win_sym)
    if s is None:
        continue
    win_addrs.append(s.address)
    # callers = list(bv.get_callers(s.address))
    # assert len(callers) == 1, callers
    # win = callers[0].function.start

# Prevent recursion
for f in bv.functions:
    for site in f.caller_sites:
        if site.function == f:
            print(f"{site.function} calls {f}")
            print(f"Avoiding {site.address:x}")
            avoid_addrs.append(site.address)

for avoid_sym in avoid_syms:
    s = bv.get_symbol_by_raw_name(avoid_sym)
    if s is None:
        continue
    callers = list(bv.get_callers(s.address))
    assert len(callers) == 1, callers
    avoid = callers[0].function.start
    avoid_addrs.append(avoid)

#TODO: prevent loops of multiple functions


ok = False
for i in win_addrs:
    callers = list(bv.get_callers(i))
    callers_callers = list(bv.get_callers(callers[0].function.start))

    if len(callers_callers) > 0:
        ok = True
        break

if not ok:
    print("WIN FUNCS HAVE NO CALLERS????")
    exit(1)


with open('target', 'w') as f:
    json.dump({
        'win': win_addrs,
        'avoid': avoid_addrs,
    }, f)
