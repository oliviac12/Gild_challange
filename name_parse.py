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
        name = self.name.replace('. ', '.')
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
                parsed_name = pp.parse(newstr)
                for i in parsed_name:
                    if i[1] == 'Surname':
                        last_name = i[0].strip(',')
                    elif i[1] == 'GivenName':
                        first_name = i[0]
                    else:
                        pass
                self.parsed_name = (first_name, last_name.replace('.', '. '))

            else:
                parsed_name = pp.parse(name)
                for i in parsed_name:
                    if i[1] == 'Surname':
                        last_name = i[0].strip(',')
                    elif i[1] == 'GivenName':
                        first_name = i[0]
                    else:
                        pass
                self.parsed_name = (first_name, last_name.replace('.', '. '))
