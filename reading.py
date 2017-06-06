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
from pdf import convert_pdf_to_txt
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
genderize = Genderize(
    user_agent='GenderizeDocs/0.0',
    api_key='975a684e9aa098d9ef7224b8c28eeb96')

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
remove=['Conference','Proceedings','International Organization International Organization','JOP','AJPS  JOP','AJPS  APSR  ','International Organization','Journal of Democracy','Political Economics','Journal of Economic History, ','-','American Political Science Review','International Studies Quarterly',"APSR","AJPS","Journal","Quarterly", "Review",'Political Analysis',"World Politics",'American Journal of Political  Science',"Comparative Political Studies" ,"Political Analysis" ,". ","American Political Science","Perspectives on Politics",' '," Comparative Politics","Political Psychology" ]

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)



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

def get_author_details(lst):

    first_name= get_Name(lst)[0]
    second_name=get_Name(lst)[1]
    probability= compute_gender(first_name)
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
    print s.values()
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
    with open('demo.csv', 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(['author','year','title','Author1Firstname','Author1Lastname','Author2Firstname','Author2Lastname','Author3Firstname','Author3Lastname','Author4Firstname','Author4Lastname','Author5Firstname','Author5Lastname'])
        writer = csv.DictWriter(f, fieldnames=['syllabus_number','publisher','year','title','Author1Firstname','Author1Lastname','Author1Gender','Author1Probability','Author2Firstname','Author2Lastname','Author2Gender','Author2Probability','Author3Firstname','Author3Lastname','Author3Gender','Author3Probability','Author4Firstname','Author4Lastname','Author4Gender','Author4Probability','Author5Firstname','Author5Lastname','Author5Gender','Author5Probability','Journal','volume','number','pages'])
        writer.writerow(dict_to_utf(mydict))

def make_csv1(mydict):
    with open('demo.csv', 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(['author','year','title','Author1Firstname','Author1Lastname','Author2Firstname','Author2Lastname','Author3Firstname','Author3Lastname','Author4Firstname','Author4Lastname','Author5Firstname','Author5Lastname'])
        writer = csv.DictWriter(f, fieldnames=['syllabus_number','publisher','year','title','Author1Firstname','Author1Lastname','Author1Gender','Author1Probability','Author2Firstname','Author2Lastname','Author2Gender','Author2Probability','Author3Firstname','Author3Lastname','Author3Gender','Author3Probability','Author4Firstname','Author4Lastname','Author4Gender','Author4Probability','Author5Firstname','Author5Lastname','Author5Gender','Author5Probability','Journal','volume','number','pages'])
        writer.writerow(dict_to_utf(mydict))

def make_csv_undecode(string):
    resultFile = open("undecode.csv", 'a')
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(string)

def remove_spaces(string):
    y = [s.replace('\n', "", 1) for s in string]
    z = [s.replace('\xe2\x80\x99s', "", 1) for s in y]
    p= [s.replace('\xe2\x80\x9c', "", 1) for s in z]
    u= [s.replace('\xe2\x80\x9d ', "", 1) for s in p]
    return u

def find_ext(dr, ext):
    return glob(path.join("/Users/dipit/Documents/RA/RA/AmericanPolitics","*.{}".format(ext)))


def get_multiple_pdf(test):
    for i in test:
        pdf=convert_pdf_to_txt(i)
        split_string = pdf.split(" \n\n")
        titles.extend (get_name(split_string))
    return titles

# titi = get_multiple_pdf(find_ext('.','pdf'))
# print titi

new_list=[]
mylist = []
def get_article_Citations(lst):
    for l in lst:
        match = re.match(r'.*([1-3][0-9]{3})', l)
        if match is not None:
            new_list.append(l)

    return new_list

def get_book_Citations(lst):
    for l in lst:
        match = re.match(r'.*([1-3][0-9]{3})', l)
        if match is None:
            mylist.append(l)
    return mylist

def get_pdf():
    pdf = convert_pdf_to_txt("/Users/dipit/Desktop/pdf/test5-split.pdf")
    # print pdf
    split_string= pdf.split(".\n\n")
    print split_string
    titles=get_name(split_string)
    return titles

ti=get_pdf()
g=[]
fTags=[]
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

new=[]
def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return izip(prevs, items, nexts)

def get_italic_titles(soup):
    for i in soup.find_all('span', style=lambda x: x and 'Italic' in x):
        bTags2.append(i.text)
    for i in bTags2:
        fTags.append(i.encode('utf-8'))
    for i in fTags:
        g.append(re.sub(r'\s', ' ', i))

    for i in g:
        for s in remove[:]:
            if similar(i,s)>0.90:
                try:
                    g.remove(i)
                except ValueError:
                    pass

    for j in g[:]:
        if j.startswith('Journal') or j.endswith('Science'):
            g.remove(j)
        elif 'Journal' in j:
            g.remove(j)
        elif j[0].isdigit():
            g.pop(g.index(j))
        elif len(j)<=2:
            g.remove(j)
        elif "Review" in j:
            g.pop(g.index(j))
        elif j.endswith("Analysis"):
            g.remove(j)
            # g.remove(len(g)-1)

    # return g
    for previous, item, nxt in previous_and_next(g):
        # print item[-1],previous
        if item[-1] == ","  or item[-1]=='--' or item[-1]==' ':
            try:
                new.append (item + nxt)
            except TypeError:
                pass
        elif item[0] == "," or item[0]==' ':
            try:
                new.append(previous + item)
            except TypeError:
                pass
        else:
            new.append(item)

    return new

def only_italic_titles(soup):
    for i in soup.find_all('span', style=lambda x: x and 'Italic' in x):
        bTags2.append(i.text)
    for i in bTags2:
        fTags.append(i.encode('utf-8'))
    for i in fTags:
        g.append(re.sub(r'\s', ' ', i))

    for i in g:
        for s in remove[:]:
            if similar(i,s)>0.90:
                try:
                    g.remove(i)
                except ValueError:
                    pass

    for j in g[:]:
        if j.startswith('Journal') or j.endswith('Science'):
            g.remove(j)
        elif 'Journal' in j:
            g.remove(j)
        elif j[0].isdigit():
            g.pop(g.index(j))
        elif len(j)<=2:
            g.remove(j)
        elif "Review" in j:
            g.pop(g.index(j))
        elif j.endswith("Analysis"):
            g.remove(j)
            # g.remove(len(g)-1)

    return g

itatics_titles= get_italic_titles(BeautifulSoup(open("/Users/dipit/Desktop/test1.html")))
# titles_articles=get_article_Citations(get_pdf())
titiles_books=get_pdf()
# only_italics=only_italic_titles(BeautifulSoup(open("/Users/dipit/Documents/RA/RA/PoliticalTheory/13600009.html")))

n=[]
def quotes_from_pdf12():
    string= convert_pdf_to_txt("/Users/dipit/Desktop/pdf/test4-split.pdf")
    # print string
    split_string = string.split("\n\n")
    # print split_string
    for i in split_string:
        if "\xe2\x80\x9c".decode("utf-8") in i:
            n.append(i)
        elif '"' in i:
            n.append(i)
        elif "‘" in i:
            n.append(i)
    # for i in new[:]:
    #     if i==' ':
    #         new.remove(i)
    return n

# print quotes_from_pdf12()

# ti= quotes_from_pdf12()
# print ti
# print titles_articles


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
        if i!='':
            f_n.append (get_first_name(i))
            l_n.append(get_last_word(i))
        else:
            f_n.append(get_first_name("NULL"))
            l_n.append(get_last_word("NULL"))


    print f_n, l_n
    return f_n,l_n

def compute_gender(lst):
    # try:
    #     return (genderize.get(lst))
    # except GenderizeException:
    return (Genderize().get(lst))


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


titi=get_pdf()
# t=[]
# for i in titi:
# 	t.append(a(i))
# titles_1= remove_spaces(t)
aut=[]
names=[]
dic={}
def author_details(lst):
    for i in lst:
        url="http://search.crossref.org/dois?q=" + i + "&rows=2"
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
def quotes_from_pdf():
    string= convert_pdf_to_txt("/Users/dipit/Desktop/test2-split.pdf")
    # print string

    quoted = re.compile('‘[^‘]*’')
    for value in quoted.findall(string):
        n.append(value)
    return n

# new_titles= quotes_from_pdf()
# print new_titles

def make_dict(lst):
    for i in lst:
        url="http://search.crossref.org/dois?q=" + i + "&rows=2"
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
        info["syllabus_number"] ="1002"
        info['publisher'] = "NULL"
        try:
            info['year'] = (data[0]['year'])
        except IndexError:
            info['year']= "NULL"
        try:

            info['title'] = (data[0]['title'])
        except IndexError:
            info['title'] = "NULL"

        try:
            dic['authors'] =(data[0]['fullCitation']).split("'")[0]
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

        print info
        # aut =(data[1]['fullCitation']).split("'")[0]
        check= (get_authors(dic.values()))
        print check
        info['Author1Firstname'] = check[0]
        info['Author1Lastname'] = check[2]
        info['Author1Gender'] = check[1]
        info['Author1Probability'] = check[3]
        info['Author2Firstname'] = check[4]
        info['Author2Lastname'] = check[6]
        info['Author2Gender'] = check[5]
        info['Author2Probability'] = check[7]
        info['Author3Firstname'] = check[8]
        info['Author3Lastname'] = check[10]
        info['Author3Gender'] = check[9]
        info['Author3Probability'] = check[11]
        info['Author4Firstname'] = check[12]
        info['Author4Lastname'] = check[14]
        info['Author4Gender'] = check[13]
        info['Author4Probability'] = check[15]
        info['Author5Firstname'] = check[16]
        info['Author5Lastname'] = check[18]
        info['Author5Gender'] = check[17]
        info['Author5Probability'] = check[19]

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
        # time.sleep(5)

        with open('result.json', 'a') as fp:
            json_text = json.dumps(info, indent=4)
            fp.write("{}\n".format(json_text))


            # make_csv(info)
info3={}
dic1={}
def get_from_google_books(lst):
    # print len(lst[6])
    for i in lst[:]:
        if len(i)>1:
            url = "https://www.googleapis.com/books/v1/volumes?q=" + i + "&maxResults=1&key=AIzaSyBADXkcoLOBG2UsddOpliFOq-JzEbbJ7_0"
            print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())

            info3["syllabus_number"]="xxxxxxx"
            try:

                info3['publisher'] = (data['items'][0]['volumeInfo']['publisher'])
            except KeyError:
                info3['publisher'] = " "
            except IndexError:
                info3['publisher'] = " "

            try:
                info3['year']= parser.parse(data['items'][0]['volumeInfo']['publishedDate']).year
            except ValueError:
                info3['year']= " "
            except KeyError:
                info3['year'] = " "

            try:
                dic1['author'] = (data['items'][0]['volumeInfo']['authors'])
            # except KeyError:
                # dic1['author'] = (data['items'][1]['volumeInfo']['authors'])
            except KeyError:
                dic1['author']= "NULL"
            pprint (dic1['author'])

            try:
                info3['pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info['pages'] = " "

            try:
                info3['title'] = (data['items'][0]['volumeInfo']['title'])
            except KeyError:
                info3['title']= "NULL"




            x= (dic1['author'])
            print x
            length = len(x)
            d = count - length
        #
            if len(x) < count:
                try:
                    x.extend(["NULL"] * d)
                except AttributeError:
                    x=" "
            else:
                pass
            check= get_author_details(x)
            print check
            info3['Author1Firstname'] = check[0]
            info3['Author1Lastname'] = check[2]
            info3['Author1Gender'] = check[1]
            info3['Author1Probability']=check[3]
            info3['Author2Firstname'] = check[4]
            info3['Author2Lastname'] = check[6]
            info3['Author2Gender'] = check[5]
            info3['Author2Probability'] = check[7]
            info3['Author3Firstname'] = check[8]
            info3['Author3Lastname'] = check[10]
            info3['Author3Gender'] = check[9]
            info3['Author3Probability'] = check[11]
            info3['Author4Firstname'] = check[12]
            info3['Author4Lastname'] = check[14]
            info3['Author4Gender'] = check[13]
            info3['Author4Probability'] = check[15]
            info3['Author5Firstname'] = check[16]
            info3['Author5Lastname'] = check[18]
            info3['Author5Gender'] = check[17]
            info3['Author5Probability'] = check[19]

            info3['Journal']= "NULL"
            info3['volume']= "NULL"
            info3['number']="NULL"
            try:
                info3['pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info3['pages'] ="NULL"

            if info3["title"] =="NULL":
                make_csv_undecode([info3["syllabus_number"],i])

            pprint (info3)
            time.sleep(6)
            with open('result.json', 'w') as fp:
                json.dump(info3, fp)


            # make_csv1(info3)

            # print undecode

# print titles_articles
# get_from_google_books(titles_books)


# get_from_google_books(only_italics)
# make_dict(titiles_books)


#
# for i in itatics_titles:
#     if 'Conference' in i or 'IEEE' in i:
#         itatics_titles.remove(i)


# print itatics_titles
# get_from_google_books(itatics_titles)
# print titles
# get_from_google_books(titiles_books)
# print ti
make_dict(ti)


def csv2json():
    csvfile = open('demo.csv', 'r')
    jsonfile = open('spark.json', 'a')

    fieldnames = ('syllabus_number','publisher','year','title','Author1Firstname','Author1Lastname','Author1Gender','Author1Probability','Author2Firstname','Author2Lastname','Author2Gender','Author2Probability','Author3Firstname','Author3Lastname','Author3Gender','Author3Probability','Author4Firstname','Author4Lastname','Author4Gender','Author4Probability','Author5Firstname','Author5Lastname','Author5Gender','Author5Probability','Journal','volume','number','pages')
    reader = csv.DictReader( csvfile, fieldnames)
    for row in (reader):
        json.dump(row, jsonfile,encoding='latin1')
        jsonfile.write('\n')



# csv2json()
# def reformat_json(input_path, output_path):
#     with open(input_path, 'r') as handle:
#         jarr = json.load(handle)
#
#     f = open(output_path, 'a')
#     for entry in jarr:
#         f.write(json.dumps(entry)+"\n")
#     f.close()


# csv2json()
# reformat_json("/Users/dipit/Documents/RA/RA/spark.json","/Users/dipit/Documents/RA/RA/spark1.json")

