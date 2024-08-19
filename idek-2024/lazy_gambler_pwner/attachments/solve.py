import angr
import base64
import json

import logging
logging.getLogger('angr.engines.unicorn_engine').setLevel('DEBUG')

with open('target', 'r') as f:
    data = json.load(f)
    win_addrs = data['win']
    avoid_addrs = data['avoid']


def sol_found(sol: bytes, addr: int):
    solution = sol.split(b'\x00')
    solution = filter(None, solution)
    solution = filter(lambda x: all(0x20<=i<=0x7f for i in x), solution)
    solution = filter(lambda x: len(x) == 7, solution)
    solution = b'\n'.join(list(solution)) + b'\n'
    solution = base64.b64encode(solution).decode()

    with open('solution', 'w') as f:
        json.dump({'solution_b64': solution, 'addr': addr}, f)
    exit(0)

class Explorer(angr.exploration_techniques.Explorer):
    def step(self, simgr, stash="active", **kwargs):
        out: angr.sim_manager.SimulationManager = super().step(simgr, stash, **kwargs)
        if len(out.unconstrained) > 0:
            for i in out.unconstrained:
                print(i.addr)
                sol_found(i.posix.dumps(0), i.addr)
        return out

    def filter(self, simgr, state: angr.SimState, **kwargs):
        out = super().filter(simgr, state, **kwargs)
        if out is None:
            print(state.history.block_count)
            if state.history.block_count > 200:
                return self.avoid_stash
        return out



proj = angr.Project('code.bin')
options = angr.options.unicorn
options.add(angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY)
options.add(angr.options.FAST_REGISTERS)
init_state = proj.factory.entry_state(add_options=options)
init_state.libc.buf_symbolic_bytes = 0x100
simulation = proj.factory.simgr(init_state)
simulation.use_technique(Explorer())
simulation.explore(find=win_addrs, avoid=avoid_addrs)
if not simulation.found:
    print(simulation.unconstrained)
    print('Cannot find path')
    exit(1)
solution = simulation.found[0]
#print(simulation.found)
solution_bytes = solution.posix.dumps(0)
print(solution.addr)
print(type(solution.addr))
sol_found(solution_bytes, solution.addr)
#print(solution)

