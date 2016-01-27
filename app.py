import database, util, search
import google

from functools import wraps

import flask, os.path

app = flask.Flask(__name__)
user = util.UserAbstraction(flask.session)
s = flask.session
r = flask.request
srcs = search.getSources()

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
    
@app.route('/profile')
@app.route('/profile/')
def profile():
    return render('profile.html')
    
@app.route('/new')
@app.route('/new/')
def new():
    return render('new.html')

@app.route("/create", methods=["GET","POST"])
@app.route("/create/", methods=["GET","POST"])
@require_login
def create():
    if r.method == "GET":
        return render('create.html')
    else:
        return render('create.html')

@app.route('/memeonic')
@app.route('/memeonic/')
@require_login
def memeonic():
    return render('memeonic.html')

@app.route('/display_infos')
@app.route('/display_infos/')
@require_login
def display_infos():
    return render('display_infos.html')

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
@require_login
def database_admin():
    return render('database_admin.html')

@app.route('/displaying', methods=["GET"])
@app.route('/displaying/', methods=["GET"])
@require_login
def displaying():
    return render('displaying.html')

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search():
    if r.method == "GET":
        return render("search.html", page_type="search")
    else:
        q = r.form["searchTerm"]
        if q:
            print q
            l = []
            results = google.search(q,num=10,start=0,stop=1)
            for url in results:
                for src in srcs:
                    if url.find(src)!=-1:
                        l.append(url)
            message = ""
            if (len(l)<2):
                message = "Timed Out: More results would take too long"
            return render("search.html", links=l, message=message, page_type="results")

# API
@app.route('/api/<action>', methods=["GET", "POST"])
@app.route('/api/<action>/', methods=["GET", "POST"])
@app.route('/api/<action>/<subaction>', methods=["GET","POST"])
@app.route('/api/<action>/<subaction>/', methods=["GET","POST"])
def api(action, subaction=None):
    if action == 'java':
        flask.abort(418)
    if r.method == 'GET':
        if action == 'info':
            return util.json_response(database.get_all_info())
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
                data = r.get_json()
                database.create_info(
                    data.get('title'),
                    data.get('body'),
                    user.id,
                    data.get('tag').split(",")
                )
                return
            if subaction == 'display_infos':
                l = get_all_info()
                return l
    flask.abort(400)

# Main Method
if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
