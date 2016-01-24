import database, util

from functools import wraps

import flask, os.path

app = flask.Flask(__name__)
user = util.UserAbstraction(flask.session)
s = flask.session
r = flask.request

# Decorators and Wrappers
def require_login(view):
    @wraps(view)
    def checked(*args, **kargs):
        if user.logged_in:
            return view(*args, **kargs)
        flask.abort(403)
    return checked

def render(template, **kargs):
    return flask.render_template(template, user=user, **kargs)

# Views
@app.route('/')
def index():
    if user.logged_in:
        return render('home.html')
    return render('index.html')

@app.route('/create')
@app.route('/create/')
def create():
    return render('create.html')

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
@require_login
def database_admin():
    return render('database_admin.html')

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search_page():
    return search.default(r.method, r.form.get('searchTerm'))

# API
@app.route('/api/<action>', methods=["GET", "POST"])
@app.route('/api/<action>/', methods=["GET", "POST"])
@app.route('/api/<action>/<subaction>', methods=["GET","POST"])
@app.route('/api/<action>/<subaction>/', methods=["GET","POST"])
def api(action, subaction=None):
    if action == 'java':
        flask.abort(418)
    if r.method == 'GET':
        if action == 'tags':
            return util.json_response(database.get_all_tags())
    if r.method == 'POST':
        if action == 'login':
            if subaction == 'dummy':
                user.log_in('Person', None)
                return flask.redirect('/')
            check = user.log_in(r.form.get('username'),
                r.form.get('password'))
            if check == None:
                return "No such username."
            if check == False:
                return "Incorrect password."
            return flask.redirect('/')
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
        if action == 'info':
            if subaction == 'create':
                return util.json_response(r.get_json())
                #database.create_info('this is the title',
                #                     'this is the body',
                #                     '1239810',
                #                     ['bio', 'sci', 'eng'])
                print database.create_info(r.form.get('title'),
                                     r.form.get('body'),
                                     84249874,
                                     list(r.form.get('tag')))
                
    flask.abort(400)

# Main Method
if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
