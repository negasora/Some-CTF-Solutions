import hashlib
import requests

seed = b'\x61\x41\x42\x43'

url = "http://the-andro-experiment.ctf.ritsec.club/ping"

h = hashlib.sha256(seed).digest()

r = requests.post(url, headers={'Content-Type': 'application/octet-stream'}, data=seed)
print(r.text)

r = requests.post(url, headers={'Content-Type': 'application/octet-stream'}, data=b'SEED:'+seed)
print(r.text)
