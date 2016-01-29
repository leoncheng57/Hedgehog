#Credit to:
#https://nlp.fi.muni.cz/projekty/random_word/index.html

import urllib2, random, json, requests

word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib2.urlopen(word_site)
txt = response.read()
all_words = txt.splitlines()

#Word Methods
def get_word(letter):
    l = []
    for word in all_words:
        if (word[0] == letter.lower() or word[0] == letter.upper()):
            l.append(word)
    return random.choice(l)    

def parse_input(equation): 
    l = []
    i = 0
    while(i<len(equation)):
        l.append( equation[i] )
        i+=1
    ret = []
    for letter in l:
        if (letter == " "):
            pass
        elif (letter == "="):
            ret.append("is")
        else:
            ret.append( get_word(letter) )
    return ret

def get_phrase(equation):
    ret = parse_input(equation)
    retString = ""
    for element in ret:
        retString+=element+" "
    return retString

#Image Methods
def get_single_image(search_term):
    api_key="e955c136382fe3c3f1ae1d1a69ca3507"
    text=search_term
    safe_search="2"
    per_page="1"
    formmat="json"
    nojsoncallback="1"
    url="https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key="+api_key+"&text="+text+"&safe_search="+safe_search+"&per_page="+per_page+"&format="+formmat+"&nojsoncallback="+nojsoncallback
    response = requests.get(url)
    json_data = json.loads(response.text)
    #now that you have the json data, go get the pic url
    #pic url :: https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
    farm_id=str(json_data["photos"]["photo"][0]["farm"])
    server_id=json_data["photos"]["photo"][0]["server"]
    idd=json_data["photos"]["photo"][0]["id"]
    secret=json_data["photos"]["photo"][0]["secret"]
    pic_url="https://farm"+farm_id+".staticflickr.com/"+server_id+"/"+idd+"_"+secret+".jpg"
    return pic_url

def get_images(equation):
    words = parse_input(equation)
    if "is" in words != -1:
        words.remove("is")
    urls = []
    for w in words:
        urls.append( get_single_image(w) )
    return urls
    
    
