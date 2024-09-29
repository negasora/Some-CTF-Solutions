import requests

url = "http://127.0.0.1:5000"


s = requests.Session()

username = 'admin'
password = 'aaaaaaaaaa'

creds_str = "username={username}&password={password}&submit=Submit"

r = s.post(url + '/signup', data=creds_str, headers={'Content-Type': 'application/x-www-form-urlencoded'})

r = s.post(url + '/login', data=creds_str, headers={'Content-Type': 'application/x-www-form-urlencoded'})


print(r.request.headers)
print(r.status_code)
print(s.cookies)

r = s.post(url + '/api/score/submit', json={'counts': [{'a':'b'} for _ in range(1000)]})
print(r.text)
print(r.json())

