from flask import Flask, render_template, request, redirect, session, url_for
import os.path, google, urllib2, bs4, re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/search", methods=["GET","POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        searchTerm = request.form["searchTerm"]
        q = searchTerm
        if q:
            print q
            l = []
            results = google.search(q,num=10,start=0,stop=10)
            for url in results:
                l.append(url)
            return str(l)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
