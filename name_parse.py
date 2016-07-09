import probablepeople as pp
import nltk
from nltk.tokenize import PunktSentenceTokenizer


class NameParse(object):
    def __init__(self, name):
        self.name = name
        self.parsed_name = None
        self._parse()

    def _parse(self):
        '''
        Assign the first and last name in self.name to self.parsed_name
        using the following format. ('first_name', 'last_name')
        '''
        custom_sent_tokenize = PunktSentenceTokenizer()
        text_file = open("title.txt", "r")
        title = text_file.read().split(',')
        name = self.name.replace('. ', '.').lower()
        tokenized = custom_sent_tokenize.tokenize(name)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            jobtil = list(set(words)&set(title))
            if len(jobtil) != 0:
                if ',' in words:
                    if words.index(jobtil[0]) < words.index(','):
                        newstr = name.split(',')[1]
                    else:
                        newstr = name.split(',')[0]
                else:
                    if words.index(jobtil[0]) == len(words)-1:
                            newstr = ' '.join(words[:-2])
                    else:
                        newstr = ' '.join(words[words.index(jobtil[0])+1:])
                self.ppname(newstr)


            else:
                self.ppname(name)

    def ppname(self, text):
        parsed_name = pp.parse(text)
        inv_parsed_name = {v: k for k, v in dict(parsed_name).items()}
        try:
            first_name = inv_parsed_name['GivenName']
            last_name = inv_parsed_name['Surname'].strip(',')
            self.parsed_name = (first_name, last_name.replace('.', '. '))
        except Exception as e:
            print str(e)
