import database

from functools import wraps

import flask, os.path
from bson import json_util

app = flask.Flask(__name__)
render = flask.render_template
session = flask.session
request = flask.request

def json_response(data):
    return flask.Response(response=json_util.dumps(data),
        status=200, mimetype='application/json')

def require_login(view):
    @wraps(view)
    def decorated(*args, **kwds):
        if session.get('logged_in') == True:
            return view
        return flask.redirect('/')
    return decorated

# Views

@app.route('/')
def index():
    return render('homepage.html')

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
@require_login
def database_admin():
    return render('database_admin.html')

###

@app.route('/home')
@app.route('/home/')
def home():
    return render('home.html')

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search_page():
    return search.default(request.method, request.form.get('searchTerm'))

# Main Method

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
