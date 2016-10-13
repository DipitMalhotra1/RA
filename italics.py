
# -- coding: UTF-8 --
import sys
import csv
import numpy as np
import openpyxl as pyxl
from itertools import tee, islice, chain, izip
from convert_2_excel import make_table

from nameparser.parser import HumanName
import nltk
import re
from convert_2_excel import remove_numbers
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
soup = BeautifulSoup(open("/Users/dipit/Documents/RA/RA/test.html"))

bTags = []
fTags=[]
res=[]
for i in soup.find_all('span', style=lambda x: x and 'Italic' in x):


    bTags.append(i.text)


# print bTags

for i in bTags:
    fTags.append(i.encode('utf-8'))
remove_num= remove_numbers(fTags)
print remove_num
for i in remove_num:
    if i == '' or len(i)==0 or len(i)==1:
        res.append(i)
final_names = list(set(remove_num) - set(res))
print len(final_names)
# print final_names
make_table([final_names])


########################################To join italics##################

test = []


# def extract_italics(inp):
#     for previous, item, nxt in previous_and_next(inp):
#         if item[-1] == ",":
#             test.append(previous + item)
#
#     return uni(test)
#
# print extract_italics(bTags)


# for i in range(len(x)):
#     scholar = "python scholar.py -c 1 --author " '" "' + "--phrase" + "'{}'".format(str(x[i]))
#     print scholar
#     if os.system(scholar):
#         os.system(scholar)