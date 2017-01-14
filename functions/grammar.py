import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

from functions.scrapper import Scrape


class Grammar(object):
    def __init__(self, path):
        self.path = path

    def grammar(self):
        inp = open(self.path, 'r').read()
        inp = [i for i in inp.split() if i not in stopwords.words('english')]
        sub = inp.pop(0)
        inp = ' '.join(inp)
        token = PunktSentenceTokenizer().tokenize(inp)
        inp1 = [i.lower() for i in inp.split()]
        while True:
            search = str(input('Enter search word\n')).lower()
            if search not in inp1:
                print('Your word isn\'t present. Try again')
            else:
                pos = []
                for i in token:
                    tok = nltk.word_tokenize(i)
                    named = nltk.pos_tag(tok)
                    pos.extend([j for i, j in named if i.lower() == search])
                pos = list(set(['Noun' for i in pos if re.search('N', i)]))

                scrapped = Scrape(search, sub).scrape()
                break

        return search, pos, scrapped
