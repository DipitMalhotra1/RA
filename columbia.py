
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
from openpy import plain2txt
from italics import get_italic_titles
import string
import re
identity = string.maketrans("", "")
from bs4 import BeautifulSoup
from italics import in_quotes

months= ['January ','February ','March ','April ', 'May ','June ','July ', 'August ', 'September ','October ','November ','December ','nd','ed','K','L','',' ','J','nd ', 'May/June ','July/ August ','Winter ', 'Spring ', 'Autumn ','ed ']
names=[]
title=[]
bTags2=[]
fTags1=[]
soup = BeautifulSoup(open("/Users/dipit/Documents/RA/RA/Columbia/200051/200051.html"))
soup1 = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/Columbia/200051/200051.pdf")
# print soup1
# title.append(soup1)
# print title
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


def in_period(string):
    s=string.split('\n')
    # return s
    for i in s:
        title.append(between(i,'. ','. '))
        title.append(between(i,'. ',' '))
    return title

after_pdf= in_period(soup1)

def remove_numbers(string):
    y = [s.translate(identity, "0123456789:-") for s in string]
    y = [s.translate(identity, "\n.\xe2\x80\x9c()") for s in y]

    for i in y[:]:
    	if len(i)<10:
    		y.remove(i)
    return  y
after_edit= remove_numbers(after_pdf)

def extract_columbia(t):
	for i in t:
		if i[0]==' ':
			names.append(i)
	return names

def line_continued(t):
	for i in t:
		return re.findall('\d*\D+',i)

print "\n\n\n\n"

quotes2txt(in_quotes(soup1))
# plain2txt(extract_columbia(after_edit))
italics2txt(get_italic_titles())


# title.append(extract_columbia(in_period(remove_numbers(title))))
# print title

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