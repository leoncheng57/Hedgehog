#Credit to:
#https://nlp.fi.muni.cz/projekty/random_word/index.html

import urllib2, random
from flask import request

speech_types = ['verbs', 'nouns', 'adjecs']
word_forms = ['norm', 'use']
probs= ['true','false']


def custom_word(speech_type, word_form, length, probability):
    #url="https://nlp.fi.muni.cz/projekty/random_word/run.cgi?language_selection=en&word_selection=verbs&model_selection=norm&length_selection=9&probability_selection=true"
    url="https://nlp.fi.muni.cz/projekty/random_word/run.cgi?language_selection=en&word_selection="+speech_type+"&model_selection="+word_form+"&length_selection="+length+"&probability_selection="+probability
    request = urllib2.urlopen(url)
    result = request.read()
    result = result[:-1] #getting rid of the \newline at the end
    result = str(result)
    print result
    return result
    
def random_word():
    speech_type = random.choice(speech_types)
    word_form = random.choice(word_forms)
    probability = random.choice(probs)
    length = random.randint(4,15)
    length = str(length)
    return custom_word(speech_type, word_form, length, probability)

def letter_word(letter):
    while (True):
        word = random_word()
        first = word[0]
        if (first == letter or first == letter.upper()):
            print word+"!"
            return word


######TESTING######
letter_word("p")
