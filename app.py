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
    def checked(*args, **kwds):
        if session.get('logged_in') == True:
            return view()
        return flask.abort(403)
    return checked

# Views

@app.route('/')
def index():
    return render('homepage.html')

@app.route('/api/<action>', methods=["GET", "POST"])
@app.route('/api/<action>/', methods=["GET", "POST"])
def api(action):
    if action == 'java':
        flask.abort(418)
    if request.method == 'GET':
        if action == 'tags':
            return json_response(database.get_all_tags())
    if request.method == 'POST':
        if action == 'login':
            check = database.verify_user(request.form.get('username'),
                request.form.get('password'))
            if check == None:
                return "No such username."
            elif check == False:
                return "Incorrect password."
            else:
                session['logged_in'] = True
                session['id'] = check.get('id')
                session['user'] = check.get('user')
                response = flask.redirect('/')
                response.set_cookie('hedgehog', json_util.dumps(check))
                return response
        if action == 'logout':
            session['logged_in'] = False
            session['id'] = session['user'] = None
            response = flask.redirect('/')
            response.set_cookie('hedgehog', max_age=0)
            return response
    flask.abort(400)

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
@require_login
def database_admin():
    return render('database_admin.html', user=session.get('user'))


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
