import database, util

from functools import wraps

import flask, os.path

app = flask.Flask(__name__)
user = util.UserAbstraction(flask.session)
render = flask.render_template
s = flask.session
r = flask.request

# Decorators
def require_login(view):
    @wraps(view)
    def checked(*args, **kwds):
        if user.logged_in:
            return view(*args, **kwds)
        flask.abort(403)
    return checked

# Views
@app.route('/')
def index():
    return render('homepage.html')

@app.route('/home')
@app.route('/home/')
def home():
    return render('home.html')

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
@require_login
def database_admin():
    return render('database_admin.html', user=user.name)

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search_page():
    return search.default(r.method, r.form.get('searchTerm'))

# API
@app.route('/api/<action>', methods=["GET", "POST"])
@app.route('/api/<action>/', methods=["GET", "POST"])
def api(action):
    if action == 'java':
        flask.abort(418)
    if r.method == 'GET':
        if action == 'tags':
            return util.json_response(database.get_all_tags())
    if r.method == 'POST':
        if action == 'login':
            check = user.log_in(r.form.get('username'),
                r.form.get('password'))
            if check == None:
                return "No such username."
            if check == False:
                return "Incorrect password."
            response = flask.redirect('/')
            response.set_cookie('hedgehog', json_util.dumps(check))
            return response
        if action == 'logout':
            user.log_out()
            response = flask.redirect('/')
            response.set_cookie('hedgehog', max_age=0)
            return response
        if action == 'register':
            check = user.create(r.form.get('username'),
                r.form.get('password'))
            if check == False:
                return "User already exists."
            else:
                return flask.redirect('/')
    flask.abort(400)

# Main Method
if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
