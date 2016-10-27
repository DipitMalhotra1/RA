import urllib, json
import time
from sortedcontainers import SortedDict
from os import path
from glob import glob
from openpy import get_name
from pprint import pprint
from pdf import convert_pdf_to_txt
from openpy import get_name
import scholarly
import csv
import numpy as np
import openpyxl as pyxl
import string
import re
from genderize import Genderize
first_name=[]
last_name=[]
info1={}
info={}
info2={}
a_name=[]
names=[]
count=5
titles=[]
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

def get_author_details(lst):

    first_name= get_Name(lst)[0]
    second_name=get_Name(lst)[1]
    # print first_name,second_name
    # probability= compute_gender(first_name)
    for x in range(len(lst)):
        info2["author{0}_firstname".format(x)]= first_name[x]
        info2["author{0}_lastname".format(x)]=  second_name[x]
        # info2["author{0}_gender".format(x)]=  probability[x]['gender']
        # try:
        #     info2["author{0}_maleprob".format(x)]=  probability[x]['probability']
        # except KeyError:
        #     info2["author{0}_maleprob".format(x)]= 0.0
        # info2["author{0}_femaleprob".format(x)] = float("{0:.2f}".format(1.0 - info2["author{0}_maleprob".format(x)]))

    s = SortedDict(info2)
    return s.values()

def array_to_utf(a):
    autf = []
    i = 0
    for v in a:
        if isinstance(v, unicode):
            autf.append(v.encode('utf-8'))
        elif isinstance(v, dict):
            autf.append(dict_to_utf(v))
        elif isinstance(v, list):
            autf.append(array_to_utf(v))
        else:
            autf.append(v)
    return autf


def dict_to_utf(d):
    dutf = {}
    for k,v in d.iteritems():
        if isinstance(v, unicode):
            dutf[k] = v.encode('utf-8')
        elif isinstance(v, list):
            dutf[k] = array_to_utf(v)
        elif isinstance(v, dict):
            dutf[k] = dict_to_utf(v)
        else:
            dutf[k] = v
    return dutf


def make_csv(mydict):
    with open('mydata.csv', 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(['author','year','title','author1_firstname','author1_lastname','author2_firstname','author2_lastname','author3_firstname','author3_lastname','author4_firstname','author4_lastname','author5_firstname','author5_lastname'])
        writer = csv.DictWriter(f, fieldnames=['year','title','author1_firstname','author1_lastname','author2_firstname','author2_lastname','author3_firstname','author3_lastname','author4_firstname','author4_lastname','author5_firstname','author5_lastname','Journal','volume','number','pages'])
        writer.writerow(dict_to_utf(mydict))


def remove_spaces(string):
    y = [s.replace('\n', "", 1) for s in string]
    z = [s.replace('\xe2\x80\x99s', "", 1) for s in y]
    p= [s.replace('\xe2\x80\x9c', "", 1) for s in z]
    u= [s.replace('\xe2\x80\x9d ', "", 1) for s in p]
    return u

def find_ext(dr, ext):
    return glob(path.join("/Users/dipit/Documents/RA/RA/American Politics","*.{}".format(ext)))


def get_multiple_pdf(test):
    for i in test:
        pdf=convert_pdf_to_txt(i)
        split_string = pdf.split(" \n\n")
        titles.extend (get_name(split_string))
    return titles

titi = get_multiple_pdf(find_ext('.','pdf'))


def get_pdf():
	pdf = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/American Politics/13300002.pdf")
	split_string= pdf.split(" \n\n")
	titles=get_name(split_string)
	return titles

def get_first_name(fullname):
    firstname = ''
    try:
        firstname = fullname.split()[0]
    except Exception as e:
        print str(e)
    return firstname


def get_last_word(string):
    try:
        return string.split()[-1]
    except IndexError:
        return "NULL"

def get_Name(lst):
	f_n=[]
	l_n=[]
	for i in lst:
		f_n.append (get_first_name(i))
		l_n.append(get_last_word(i))
	return f_n,l_n

# def compute_gender(lst):
# 	return (Genderize().get(lst))


def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def get_authors(lst):
    for i in lst:
        names= (i.split(','))
    names1 = [item.encode('utf-8') for item in names]

    for i in names1[:]:
        if i==' ' or i.lstrip().isdigit():
            # names1.remove(i):
            names1.remove(i)
    length= len(names1)
    d=count-length
    #
    if len(names1) < count:
        names1.extend(["NULL"] * d)
    # return get_Name(names1)
    return get_author_details(names1)
    # else:
    #     return get_author_details(names1)
    # return get_author_details(names1)

# titi=get_pdf()
t=[]
for i in titi:
	t.append(a(i))
titles_1= remove_spaces(t)
aut=[]
names=[]
dic={}
def author_details(lst):
    for i in lst:
        url="http://search.crossref.org/dois?q=" + i + "&rows=3"
        response = urllib.urlopen(url)
        try:
            data = json.loads(response.read())
        except ValueError:
            data=" "
        dic['authors'] =(data[1]['fullCitation']).split("'")[0]
        # pprint (aut)
        #  (dic.values())
        pprint (get_authors(dic.values()))
        # pprint(dic)

# print author_details(titi)

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]

def between(value, a, b):
    # Find and validate before-part.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    # Find and validate after part.
    pos_b = value.rfind(b)
    if pos_b == -1: return ""
    # Return middle part.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= pos_b: return ""
    return value[adjusted_pos_a:pos_b]
test={}
def make_dict(lst):
    for i in lst:
        url="http://search.crossref.org/dois?q=" + i + "&rows=3"
        print url
        try:
            response = urllib.urlopen(url)
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise # Not error we are looking for
            pass 
        try:
            data = json.loads(response.read())
        except ValueError:
            data=" "
        try:
            info['year'] = (data[1]['year'])
        except IndexError:
            info['year']= "NULL"

        try:

            info['title'] = (data[1]['title'])
        except IndexError:
            info['title'] = "NULL"

        try:
            dic['authors'] =(data[1]['fullCitation']).split("'")[0]
        except IndexError:
            dic['authors']= "NULL"        # print dic


        try:
            x= (data[1]['fullCitation'])
        except IndexError:
            x= "NULL"
        try:
            journal= (between(x,'<i>','</i>'))
        except IndexError:
            journal ="NULL"

        try:
            journal_page= after(x,"</i>").split(",")
        except IndexError:
            journal_page="NULL"


        # aut =(data[1]['fullCitation']).split("'")[0]
        check= (get_authors(dic.values()))
        info['author1_firstname'] = check[0]
        info['author1_lastname'] = check[1]
        info['author2_firstname'] = check[2]
        info['author2_lastname'] = check[3]
        info['author3_firstname'] = check[4]
        info['author3_lastname'] = check[5]
        info['author4_firstname'] = check[6]
        info['author4_lastname'] = check[7]
        info['author5_firstname'] = check[8]
        info['author5_lastname'] = check[9]

        info['Journal']= journal
        try:
            info['volume']= journal_page[-3]
        except IndexError:
            info['volume'] = " "
        try:
            info['number']= journal_page[-2]
        except IndexError:
            info['number'] = " "

        
        try:
            info['pages']= journal_page[-1]
        except IndexError:
            info['pages']= " "
       
   
        # info['Journal_info'] = journal_page


        pprint (info)
        time.sleep(7) 
        make_csv(info)

make_dict(titles_1)
