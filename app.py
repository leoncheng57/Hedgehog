from flask import Flask, Response, render_template, request, redirect, session, url_for
import os.path, google, urllib2, bs4, re, database
from bson import json_util

app = Flask(__name__)

#Putting all Outside Sources into list 'srcs'
f = open("Sources.txt", "r")
srcs = []
for line in f:
    line = line[0:-1] #-1 is to remove the newline character
    line = line.replace("https","")
    line = line.replace("http","")
    line = line.replace("//","")
    line = line.replace(":","")
    line = line.replace("www.","")
    srcs.append(line)

@app.route('/')
def index():
    return render_template('homepage.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/datas', methods=["GET"])
@app.route('/datas/', methods=["GET"])
def datas():
    return render_template('datas.html')

@app.route('/request', methods=["GET"])
@app.route('/request/', methods=["GET"])
def request_api():
    return Response(response=json_util.dumps(database.get_all_tags()),
    status=200, mimetype='application/json')

@app.route("/search", methods=["GET","POST"])
@app.route("/search/", methods=["GET","POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        q = request.form["searchTerm"]
        if q:
            print q
            l = []
            results = google.search(q,num=10,start=0,stop=25)
            for url in results:
                for src in srcs:
                    if url.find(src)!=-1:
                        l.append(url)
            message = ""
            if (len(l)<2):
                message = "Timed Out: More results would take too long"
            return render_template("links.html", links=l, message=message)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
