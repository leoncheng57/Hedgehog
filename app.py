from flask import Flask, Response, render_template, request, redirect, session, url_for
import os.path, google, urllib2, bs4, re, database, search
from bson import json_util

app = Flask(__name__)

def jsonResponse(data):
    return Response(response=json_util.dumps(data),
        status=200, mimetype='application/json')

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/api/<data>', methods=["GET", "POST"])
@app.route('/api/<data>/', methods=["GET", "POST"])
def api(data):
    return "WIP"

@app.route('/database', methods=["GET"])
@app.route('/database/', methods=["GET"])
def datas():
    return render_template('database_admin.html')

@app.route('/home')
@app.route('/home/')
def home():
    return render_template('home.html')

###

@app.route('/request', methods=["GET"])
@app.route('/request/', methods=["GET"])
def request_api():
    return_type = request.args.get('type')
    if return_type == 'tags':
        data = database.get_all_tags()
    elif return_type == 'info':
        data = database.get_top_level_tags() # Eheh, need another function to put here...
    return jsonResponse(data)

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search_page():
    return search.default(request.method, request.form.get('searchTerm'))

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
