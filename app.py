from flask import Flask, render_template, request, redirect, session, url_for
import os.path, google, urllib2, bs4, re

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
    return render_template('index.html')

@app.route("/search", methods=["GET","POST"])
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
