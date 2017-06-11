#-- coding: UTF-8 --
import urllib, json
from itertools import tee, islice, chain, izip
from difflib import SequenceMatcher
from genderPredictor import genderPredictor
from socket import error as SocketError
import dateutil.parser as parser
import errno
import time
from sortedcontainers import SortedDict
from os import path
from glob import glob
from openpy import get_name
from pprint import pprint
# from pdf import convert_pdf_to_txt
from openpy import get_name
import scholarly
import csv
from bs4 import BeautifulSoup
import numpy as np
import openpyxl as pyxl
import string
import re
import sys
from nltk.corpus import names
from gp import get_gender
import random
from genderize import Genderize, GenderizeException
import os
# genderize = Genderize(
#     user_agent='GenderizeDocs/0.0',
#     api_key='975a684e9aa098d9ef7224b8c28eeb96')
file=[]
reload(sys)
sys.setdefaultencoding('utf-8')
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
undecode=[]
bTags2=[]
aut=[]
names=[]
dic={}

def gender_list(f):
    list1 = []
    for i in f:
        if i=="NULL":
            list1.append("NULL")
        else:
            list1.append(get_gender(i)[0])
    return list1

def gender_list_prob(f):
    list2 = []
    for i in f:
        if i=="NULL":
            list2.append("NULL")
        else:
            list2.append(get_gender(i)[1])
    return list2

def get_author_details(lst):

    first_name= get_Name(lst)[0]
    second_name=get_Name(lst)[1]
    # probability= compute_gender(first_name)
    try:
        flag= gender_list(first_name)
    except IndexError:
        flag=" "
    try:
        prob_flag= gender_list_prob(first_name)
    except IndexError:
        prob_flag = " "
    for x in range(len(lst)):
        info2["author{0}_firstname".format(x)]= first_name[x]
        info2["author{0}_lastname".format(x)]=  second_name[x]
        try:
            info2["author{0}_gender".format(x)]=  flag[x]
        except:
            info2["author{0}_gender".format(x)] = "NULL"
        try:
            info2["author{0}_prob".format(x)]= prob_flag[x]
        except KeyError:
            info2["author{0}_prob".format(x)]= 0.0

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

def get_first_name(fullname):
    firstname = ''
    try:
        firstname = fullname.split()[0]
    except Exception as e:
        print str(e)+'exception'
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
        if i!='':
            f_n.append (get_first_name(i))
            l_n.append(get_last_word(i))
        else:
            f_n.append(get_first_name("NULL"))
            l_n.append(get_last_word("NULL"))
    return f_n,l_n

def compute_gender(lst):
    # try:
    #     return (genderize.get(lst))
    # except GenderizeException:
    return (Genderize().get(lst))


def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

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
    if len(names1) < count:
        names1.extend(["NULL"] * d)
    return get_author_details(names1)


def author_details(lst):
    for i in lst:
        url="http://search.crossref.org/dois?q=" + i + "&rows=2"
        response = urllib.urlopen(url)
        try:
            data = json.loads(response.read())
        except ValueError:
            data=" "
        dic['authors'] =(data[1]['fullCitation']).split("'")[0]

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

def after(value, a):
    # Find and validate first part.
    pos_a = value.rfind(a)
    if pos_a == -1: return ""
    # Returns chars after the found string.
    adjusted_pos_a = pos_a + len(a)
    if adjusted_pos_a >= len(value): return ""
    return value[adjusted_pos_a:]


def traverse(dir):
    for dirpath, subdirs, files in os.walk(dir):
        if (files == ".DS_Store"):
            os.remove("/Users/dipit/Documents/RA/RA/Docs/PDF/" + files)
        file.extend(os.path.join(dirpath, x) for x in files)
    return file
print os.path.dirname(os.getcwd())
