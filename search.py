from flask import render_template
import google, urllib2, bs4, re

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
    
def default(method, search_term):
    if method == "GET":
        return render_template("search.html")
    else:
        q = search_term
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
