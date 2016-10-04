# -- coding: UTF-8 --
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

import nltk
import string
identity = string.maketrans("", "")
from itertools import tee, islice, chain, izip
from pdf import convert_pdf_to_txt

def extract_after_name(string):
    return string.split(string, 1)[1]

def remove_numbers(string):
    y = [s.translate(identity, "0123456789:-") for s in string]
    z =  [s.translate(identity, "\xe2\x80\xa2\x9c\x0c") for s in y]
    p =  [s.translate(identity, "\n") for s in z]
    u = [s.translate(identity, "()") for s in p]
    b = [s.translate(identity, '') for s in u]
    return b

def remove_punctuation(result):
    #
    r = ["".join(c for c in result if c not in (','))]
    # rem_numbers= [''.join([i for i in r if not i.isdigit()])]
    return r

def uni(mylist):
    t = [(el.strip()) for el in mylist]
    # x = [item.encode('utf-8') for item in t]

    return t


def split_list(text):
    sents = text.split(',')
    answer = [sent.split() for sent in sents if sent]
    return answer

check=[]

def extract():
    string = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/names.pdf")
    lines = [line.split("\n") for line in string.splitlines() if "," in line]
    # print lines
    # # print lines
    for i in lines:
        for j in i:
            rem_white = j.replace(' ', '')
            check.extend(rem_white.split(','))
    list_separate= remove_numbers(check)
    # print list_separate
    remove_space = [x for x in list_separate if x != '']
    # print remove_space
    combine_two = [remove_space[x:x + 2] for x in xrange(0, len(remove_space), 2)]
    # print combine_two

    for i in combine_two:
        scholar = "python scholar.py -c 1 --author " + '"{}"'.format(i[0]) + "--phrase  " + '"{}"'.format(i[1])
        print scholar

        # os.system(scholar)


extract()