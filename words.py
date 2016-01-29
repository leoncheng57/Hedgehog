#Credit to:
#https://nlp.fi.muni.cz/projekty/random_word/index.html

import urllib2, random

word_site = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib2.urlopen(word_site)
txt = response.read()
all_words = txt.splitlines()

def get_word(letter):
    l = []
    for word in all_words:
        if (word[0] == letter.lower() or word[0] == letter.upper()):
            l.append(word)
    return random.choice(l)    

#input should be an equation with spaces between every letter
def get_phrase(equation):
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
    retString = ""
    for element in ret:
        retString+=element+" "
    return retString


###TESTING####
#print get_word("p")
print get_phrase("F=ma")
