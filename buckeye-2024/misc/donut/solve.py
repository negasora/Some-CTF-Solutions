from pwn import remote, context

r = remote("challs.pwnoh.io", 13434)

stacks = [[], [], []]
stack_idx = 0
for line in r.recv().splitlines():
    line = line.strip()
    if line == b'|':
        continue
    if line == b'':
        stack_idx += 1
        if stack_idx == 3:
            break
        continue

    stacks[stack_idx].insert(0, line.count(b'-')//2)

#stacks = [[], [], []]

moves: list[tuple[int, int]] = []
def hanoi(n: int, X: int):
#move all disks of size n or less to spindle X:
    # Base case: If we need to move zero disks, there's nothing to do.
    if n == 0:
        return

    # Recursive case 1: If disk n is already on spindle X, we don't need to
    # do anything fancy! Just move the other disks.
    #if disk n is on spindle X:
    if n in stacks[X]:
        #recursively move all disks of size n-1 to spindle X
        hanoi(n-1, X)
        return

    # Recursive case 2: If disk n isn't on spindle X, it's on some other
    # spindle Y. That means all other disks need to get to the third
    # spindle Z before we can move disk n.
    #recursively move all disks of size n-1 to spindle Z, as defined above.
    #move disk n to spindle X.
    for Y, contents in enumerate(stacks):
        if n in contents:
            # 0 and 1 -> 2, 0 and 2 -> 1, 1 and 2 -> 0
            Z = len(stacks) - (Y+X)
            assert Z != X and Z != Y
            hanoi(n-1, Z)
            print(stacks)
            removed = stacks[Y].pop()
            assert removed == n
            print(f"{len(moves)}: moving {n} from {Y} to {X}")
            moves.append((Y+1, X+1))
            assert len(stacks[X]) == 0 or stacks[X][-1] > n, stacks
            stacks[X].append(n)
            break

    # Now, move all the remaining disks back on top of disk n.
    #recursively move all disks of size n-1 to spindle X.
    hanoi(n-1, X)

print(stacks)
hanoi(10, 2)
print(stacks)

solution_string = b''

for i,(f,t) in enumerate(moves):
    solution_string += str(f).encode() + b'\n'
    solution_string += str(t).encode() + b'\n'

r.sendline(solution_string)
r.recvuntil(b'bctf', drop=True)
print((b'bctf' + r.recvline()).decode())
