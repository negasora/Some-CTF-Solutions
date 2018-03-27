"""
All endpoints are on http://broadcastr.chal.csaw.io:4000

GET /api/user/info

Requires user:info:read scope

Returns JSON

    username - User's name
    email - User's email

POST /api/user/info/update

Requires user:info:write scope

Accepts JSON

    email - The email to change to

Returns JSON

    username - User's name
    email - User's email

GET /api/user/status

Requires user:status:read scope

Returns JSON

    status - The user's last broadcasted status

GET /api/user/history

Requires user:history:read scope

Returns JSON

    history - All of the user's broadcasts
"""


import requests


s = requests.Session()

from flask import Flask, session, redirect, url_for, request, Token
from flask_oauthlib.client import OAuth
import os, datetime
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


tok = "0859abcd56d1e853d745e21872273890" #localhost oauth-authorized
#tok = "60a11522da535d88a11d710b2dd46d5d" #google





app = Flask(__name__)
oauth = OAuth()


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['BRD'] = {
    'consumer_key': tok,
    'consumer_secret': tok,
}

oauth.init_app(app)

broadcastr = oauth.remote_app('broadcastr',
    base_url='http://broadcastr.chal.csaw.io:4000/api',
    request_token_url=None,
    access_token_url='http://broadcastr.chal.csaw.io:4000/oauth/token',
    authorize_url='http://broadcastr.chal.csaw.io:4000/oauth/authorize',
    app_key='BRD',
    #consumer_secret=tok,
    request_token_params = {'scope': 'user:info:read user:status:read'}
)

@app.tokensetter
def save_token(token, request):
    expires = datetime.utcnow() + timedelta(seconds=token['expires_in'])
    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client_id=request.client.client_id,
        user_id=request.user.id,
    )
    return tok

@app.tokengetter


@app.route("/login")
def login():
    return broadcastr.authorize(callback="http://127.0.0.1:5000/oauth-authorized")
    #return broadcastr.authorize(callback="http://google.com")

@app.route("/oauth-authorized")
def oauth_authorized():

#{u'access_token': u'ximnF5j6aWPVZmnGAQiu1as2GyQ5Cc', u'token_type': u'Bearer', u'expires_in': 3600, u'refresh_token': u'6jXuNwmGmAG5VX5jLiOttznUvN6AJw', u'scope': u'user:info:read user:status:read'}
    resp = broadcastr.authorized_response()
    print resp
    session['broadcastr_token'] = resp['access_token']
    next_url = request.args.get('next') or url_for('info')
    return redirect(next_url)


@app.route("/api/user/info")
def info():

    return broadcastr.get("http://broadcastr.chal.csaw.io:4000/api/user/info", access_token=session['broadcastr_token'])

app.run()
