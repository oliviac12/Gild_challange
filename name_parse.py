import probablepeople as pp
import nltk
from nltk.tokenize import PunktSentenceTokenizer


class NameParse(object):
    def __init__(self, name):
        self.name = name
        self.parsed_name = None
        self._parse()

    # def process_content(name):
    #     name = name.replace('. ', '.')
    #     tokenized = custom_sent_tokenize.tokenize(name)
    #     for i in tokenized:
    #         words = nltk.word_tokenize(i)
    #         jobtil = list(set(words)&set(title))
    #         if len(jobtil) != 0:
    #             if ',' in words:
    #                 if words.index(jobtil[0]) < words.index(','):
    #                     newstr = name.split(',')[1]
    #                     print newstr
    #                 else:
    #                     newstr = name.split(',')[0]
    #                     print newstr
    #             else:
    #                 if words.index(jobtil[0]) == len(words)-1:
    #                         newstr = words[:-2]
    #                 else:
    #                     newstr = words[words.index(jobtil[0])+1:]
    #                     print newstr
    #             parsed_name = pp.parse(newstr)
    #             for i in parsed_name:
    #                 if i[1] == 'Surname':
    #                     last_name = i[0].strip(',')
    #                 elif i[1] == 'GivenName':
    #                     first_name = i[0]
    #                 else:
    #                     pass
    #             self.parsed_name = (name.first, name.last)
    #
    #         else:
    #             parsed_name = pp.parse(name)
    #             for i in parsed_name:
    #                 if i[1] == 'Surname':
    #                     last_name = i[0].strip(',')
    #                 elif i[1] == 'GivenName':
    #                     first_name = i[0]
    #                 else:
    #                     pass
    #             self.parsed_name = (name.first, name.last)

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
                        print newstr
                    else:
                        newstr = name.split(',')[0]
                        print newstr
                else:
                    if words.index(jobtil[0]) == len(words)-1:
                            newstr = words[:-2]
                    else:
                        newstr = words[words.index(jobtil[0])+1:]
                        print newstr
                parsed_name = pp.parse(newstr)
                for i in parsed_name:
                    if i[1] == 'Surname':
                        last_name = i[0].strip(',')
                    elif i[1] == 'GivenName':
                        first_name = i[0]
                    else:
                        pass
                self.parsed_name = (first_name, last_name)

            else:
                parsed_name = pp.parse(name)
                for i in parsed_name:
                    if i[1] == 'Surname':
                        last_name = i[0].strip(',')
                    elif i[1] == 'GivenName':
                        first_name = i[0]
                    else:
                        pass
                self.parsed_name = (first_name, last_name)
