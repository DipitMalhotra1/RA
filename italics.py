
# -- coding: UTF-8 --
import sys
import csv
import numpy as np
import openpyxl as pyxl
import nltk
import re
from itertools import tee, islice, chain, izip
from pdf import convert_pdf_to_txt
# from convert_2_excel import make_table
from nameparser.parser import HumanName
from openpy import italics2txt
from openpy import quotes2txt
from openpy import between
from openpy import get_name
from openpy import after
from convert_2_excel import remove_numbers
from bs4 import BeautifulSoup

bTags1=[]
bTags = []
fTags=[]
fTags1=[]
res=[]
test1=[]
bTags2=[]
months= ['January ','February ','March ','April ', 'May ','June ','July ', 'August ', 'September ','October ','November ','December ','nd','ed','K','L','',' ','J','nd ', 'May/June ','July/ August ','Winter ', 'Spring ', 'Autumn ','ed ']
names=[]
soup = BeautifulSoup(open("/Users/dipit/Documents/RA/RA/Columbia/200051/200051.html"))
soup1 = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/Columbia/200041/200041.pdf")
# print soup1

# def in_period(string):
#     for i in string:
#         print between(i,'. ','. ')
#
# in_period(soup1)

def in_quotes(string):
    sp= string.split('\n')
    # print sp
    for i in sp:
        bTags1.append(after(i, '“'))
    return get_name(remove_numbers(bTags1))

q_titles= in_quotes(soup1)
print q_titles


def quotes_name(r):

    quoted1 = re.compile('(.+)"[^"]+" ')
    quoted = re.compile('(.+)"[^"]+",')
    quoted2 = re.compile('(.+)"[^"]+".')

    for value in (quoted.findall(r) or quoted1.findall(r) or (quoted2.findall(r))):
        test1.append(value)
    return test1

q_name= quotes_name(soup1)

def get_italic_titles():
    for i in soup.find_all('span', style=lambda x: x and 'Italic' in x):
        bTags2.append(i.text)

    # print bTags
    for i in bTags2:
        fTags1.append(i.encode('utf-8'))
    # print fTags
    remove_num = remove_numbers(fTags1)
    print len(remove_num)
    for i in remove_num:
        if len(i)<=2:
            remove_num.remove(i)
    # for i in q_titles:
    #     remove_num.append(i)
    #     remove_num.append('')
    # print len(remove_num)
    return remove_num


def get_author_names():
    for i in soup.find_all('span', style=lambda x: x and 'PSMT' in x):
        bTags.append(i.text)
    # print bTags
    for i in bTags:
        fTags.append(i.encode('utf-8'))
    # print fTags
    remove_num = remove_numbers(fTags)
    for i in remove_num:
        res.append(i.split(','))
    for i in range(len(res)):
        names.append(res[i][0])
    # print names
    for i in names:
        if len(i) <= 3:
            names.remove(i)
    for i in names:
        if i in months:
            names.remove(i)
    for i in q_name:
        names.append(i)
    print len(names)
    return names

print get_italic_titles()
# print get_author_names()
# print "\n\n\n"



x=get_italic_titles()

# italics2txt(x)
# quotes2txt(q_titles)

# get_italic_titles()
# make_table([get_italic_titles(),get_author_names()])


########################################To join italics##################

# test = []


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