from bson import json_util
import database, search
import flask, os.path

app = flask.Flask(__name__)

def jsonResponse(data):
    return flask.Response(response=json_util.dumps(data),
        status=200, mimetype='application/json')

# Views

@app.route('/')
def index():
    return flask.render_template('homepage.html')

@app.route('/api/<data>', methods=["GET", "POST"])
@app.route('/api/<data>/', methods=["GET", "POST"])
def api(data):
    return str(dir(flask.request))

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
def datas():
    return flask.render_template('database_admin.html')

@app.route('/home')
@app.route('/home/')
def home():
    return flask.render_template('home.html')

###

@app.route('/request', methods=["GET"])
@app.route('/request/', methods=["GET"])
def request_api():
    return_type = flask.request.args.get('type')
    if return_type == 'tags':
        data = database.get_all_tags()
    elif return_type == 'info':
        data = database.get_top_level_tags() # Eheh, need another function to put here...
    return jsonResponse(data)

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search_page():
    return search.default(flask.request.method, flask.request.form.get('searchTerm'))

# Main Method

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
