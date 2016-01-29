from flask import render_template
import google, urllib2, bs4, re, os.path

def getSources(): #Putting all Outside Sources into list 'srcs'
    srcs = []
    f = open(os.path.join(os.path.dirname(__file__), "misc/sources.txt"), "r")
    for line in f:
        line = line[0:-1] #-1 is to remove the newline character
        line = line.replace("https","")
        line = line.replace("http","")
        line = line.replace("//","")
        line = line.replace(":","")
        line = line.replace("www.","")
        srcs.append(line)
    return srcs


# def default(method, search_term, srcs):      
#     d = {}
#     if method == "GET":                                                              
#         #return render("search.html", page_type="search")                               
#         return d 
#     else:                                                                              
#         q = search_term
#         if q:                                                                          
#             print q                                                                    
#             l = []                                                                     
#             results = google.search(q,num=10,start=0,stop=25)                          
#             for url in results:                                                        
#                 for src in srcs:                                                       
#                     if url.find(src)!=-1:                                              
#                         l.append(url)                                                  
#             message = ""                                                               
#             if (len(l)<2):                                                             
#                 message = "Timed Out: More results would take too long"                
#             #return render("search.html", links=l, message=message, page_type="results") 
#             d["links"] = l
#             d["message"] = message 
#             return d

