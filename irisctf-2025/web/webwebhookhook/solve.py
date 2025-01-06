import requests

url = "http://127.0.0.1:8080"

s = requests.Session()

# we need to create a webhook where URI.create(our_hook).toURL() == URI.create(https://example.com/admin).toURL() but our_hook != URI.create(https://example.com/admin).toURL() maybe

# URL equality depends if the host resolves to the same ip???

# need to find a string such that URI.create(our_hook).toURL() == URI.create(https://example.com/admin).toURL() AFTER we change something on our side - maybe a dns record?


def create(webhook_url: str):
    r = s.post(f'{url}/create', json={
        'hook': webhook_url,
        'template': 'template data: _DATA_',
        'response': 'sent ok'
        }
    )
    print(r.text)


def do_webhook(webhook_url: str, contents: str):
    r = s.post(f'{url}/webhook?hook={webhook_url}', data=contents, headers={'Content-Type': 'multipart/form-data'})
    print(r.text)

# If we can find a string that is equivalent to http://example.com/admin but openConnection goes to our host we get flag

hook = 'http://example.com/admin'

create(hook)
do_webhook(hook, '''<?xml version = "1.0" ?>
<!DOCTYPE foo [<!ENTITY foo ANY>]>
<message>aaaaaa</message>
''')
# Can we open a file:// url and write to it???
# can we write to /etc/hosts and redirect example.com to a thing we own????
# Looks like we can only open connections to things that result in HTTPUrlConnection
"""
can we:

make a dns record ctf.negasora.com pointing to our box
send a create request for it

change the record to the same as example.com

send a webhook request but hold the request open so reading blocks

change the dns record back to an ip we're listening on

finish sending request body


but will it hit example.com first and not touch ours at all?
"""
