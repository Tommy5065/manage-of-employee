from flask import Flask, request, session, redirect, url_for
from Blue.login import bp as login_bp
from Blue.index import bp as index_bp
from Blue.register import bp as register_bp
app = Flask(__name__)
app.secret_key='dev'

app.register_blueprint(login_bp)
app.register_blueprint(index_bp)
app.register_blueprint(register_bp)


def auth():
    if request.path.startswith('/static'):
        return

    if request.path == '/login' :
        return
    elif request.path == '/register':
        return
    elif request.path == '/change/password':
        return

    Session = session.get('user_info')
    if not Session:
        return redirect(url_for('login.login'))

app.before_request(auth)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
