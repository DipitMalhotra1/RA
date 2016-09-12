# # -- coding: UTF-8 --
#
# # from linecache import getline
# # with open("output.txt") as f:
# #     for ind, line in enumerate(f,1):
# #         if line.rstrip() == "Reference":
# #             print(getline(f.name, ind+1))
# #
# import re
# z='Mainwaring, Scott, and Timothy R. Scully. 1995. "Introduction: Party Systems in Latin America."'
# r='Hall, Peter A., and Soskice David. 2001. "An Introduction to Varieties of Capitalism," Varieties of Capitalism: The Institutional Foundations of Comparative Advantage. Oxford University Press, Chp. 1, pp. 1-68.'
# i='Tajfel, Henri, and John C. Turner. 2001. "The Social Psychology of Intergroup Relations " Intergroup Relations: Essential Readings, ed. Michael A. Hogg and Dominic Abrams. Psychology Press, 94-109.'
# def quotes(x):
#     quoted = re.compile('"[^"]*"')
#     for value in quoted.findall(x):
#         return value
#
# def quotes_x(x):
#     quoted = re.compile('(.+)"[^"]+"')
# #     for value in quoted.findall(x):
# #         return value
# #
# #
# # o= z+"\n" + r
# # print quotes_x()
# # print quotes(z) + "\n" + quotes_x(z)
#
#
#
# import re
# import string
#
# s ="•  Rogowski, Ronald and Mark Andreas Kayser. . "
# s = re.sub(r'[^\w\s]','',s)
# print s
#
# p= ['hello', '...', 'h3.a', 'ds4,']
# x = [''.join(x for x in par if x not in string.punctuation) for par in p]
# print x
#
# j= ['world', 'good', 'plce']
#
# print x + j
#
# z=zip(x,j)
# print "zipped:", z
# print "djc", z[1][1]
# i=0
# j=0
# for i in range(3):
#     print " test " + z[i][0]  + " succeed " + z[i][1]
#
# # for i, j in range(0,4):
# #     print  z[i][j]













from itertools import tee, islice, chain, izip

from nameparser.parser import HumanName
import nltk
import re
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)
def remove_punctuation(result):
    #
    r = ["".join(c for c in result if c not in (','))]
    # rem_numbers= [''.join([i for i in r if not i.isdigit()])]
    return r
def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

def uni(mylist):
    t = [(el.strip()) for el in mylist]
    x = [item.encode('utf-8') for item in t]

    return x

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/dipit/Documents/RA/RA/RA/myfile.html"))

bTags = []

for i in soup.find_all('span', style=lambda x: x and 'Italic' in x):


    bTags.append(i.text)


# print bTags

test = []


def extract_italics(inp):
    for previous, item, nxt in previous_and_next(inp):
        if item[-1] == ".":
            test.append(previous + item)

    return uni(test)

print extract_italics(bTags)


# for i in range(len(x)):
#     scholar = "python scholar.py -c 1 --author " '" "' + "--phrase" + "'{}'".format(str(x[i]))
#     print scholar
#     if os.system(scholar):
#         os.system(scholar)