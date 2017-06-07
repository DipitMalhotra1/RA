# # -- coding: UTF-8 --
import urllib, json
import os
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
import html
import re
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

soup = BeautifulSoup(open("/Users/dipit/Documents/RA/RA/Demo/output3.html"))
from utility import *
bTags = []
fTags=[]
new=[]
test=[]
info3={}
dic1={}
aut=[]
names=[]
dic={}
info={}
z=[]
bTags2=[]
def extract_articles():
    #CMR9# Font style
    # for i in soup.find_all('span', style=lambda x: x and 'Regular' in x): #font style: regular#
    # for i in soup.find_all('span', style=lambda x: x and 'TIM5;' in x):  #font style: Regu;#
    for i in soup.find_all('span', style=lambda x: x and 'Times-Roman' in x):  #font style: times-roman#

        fTags.append(i.text)
    fTags1=[item.encode('ascii', 'ignore') for item in fTags]
    for previous, item, nxt in previous_and_next(fTags1):
        if item[-1]=='\n':
            try:
                z.append (item + nxt)
            except TypeError:
                pass
    for i in range(len(z)-1):

        # new.extend(re.findall("\(\d{4}\)\s.([^\.]*).*",z[i]))    #Year in paranthesis followed by space#


        #new.extend(re.findall("(,)([^\.]*)(,)", z[i]))   #Different Citation style year at end#

        # new.extend(re.findall("\.\s\d{4}\.([^\.]*).*", fTags[i]))   #Year not in paranthesis preceeded by white space
        # new.extend(re.findall("\.\d{4}\.([^\.]*).*", fTags[i]))  #Year not in paranthesis#
        new.extend(re.findall("\(\d{4}\).([^\.]*).*",z[i]))    #Year in paranthesis#

    l = [item.encode('ascii', 'ignore') for item in new]
    l = [x.strip() for x in l if x.strip()]
    return l


# Works for column type citations#

joinbook = []
test2 = []


def extract_books1():
    result=[]

    # for i in soup.find_all('span', style=lambda x: x):    #if column wise cited#
    for i in soup.find_all('span', style=lambda x: x):

        bTags.append(i.text.strip())
    # print bTags
    filtered = filter(None, bTags)
    filtered=[x.strip() for x in filtered if x.strip()]
    print filtered
    print "\n\n"

    for previous,item,nxt in previous_and_next(filtered):
        if item[-7:-3].isdigit():     #(year) .#

        # if item[-5:-1].isdigit():    #(year)
            try:
                joinbook.append (item + nxt)
            except TypeError:
                pass
    for i in range(len(joinbook)):
        test2.extend(re.findall("\(\d{4}\).*", joinbook[i]))
        # try:
        #     # if re.findall("\.\d{4}", joinbook[i]) and joinbook[i][-5:-1].isdigit():
        #     #     test2.append(joinbook[i + 1])
        #     # elif re.findall("\(\d{4}\)", test[i])  and joinbook[i][-6:-2].isdigit():
        #     #     test2.append(joinbook[i+1])
        #     test2.append(re.findall("\(\d{4}\).*", joinbook[i])):
        #         # test2.append(joinbook[i])
        #
        # except IndexError:
        #     pass
    result=[item.encode('ascii', 'ignore') for item in test2]
    return result



def extract_books():  #Works for column type citations#
    test2 = []
    # for i in soup.find_all('span', style=lambda x: x):    #if column wise cited#
    for i in soup.find_all('span', style=lambda x: x):

        bTags.append(i.text.strip())
    test = filter(None, bTags)
    test=[item.encode('ascii', 'ignore') for item in test]
    print test
    print "\n\n"
    for i in range(len(test)):


        try:
            if re.findall("\.\d{4}", test[i]) and test[i][-5:-1].isdigit():
                test2.append(test[i+1])
            elif re.findall("\(\d{4}\)", test[i]) and test[i][-6:-2].isdigit() and test[i][-2]==')':
                test2.append(test[i+1])
            # elif re.findall("\d{4}\)\,\s.*", test[i])  and test[i][-6:-2].isdigit():
            #     test2.append(test[i+1])

        except IndexError:
            pass

    return test2


write_list=[]
def crossRef(lst):
    i=0
    for i in lst:
        url = "http://search.crossref.org/dois?q=" + i + "&rows=2"
        print url
        try:
            response = urllib.urlopen(url)
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
            pass
        try:
            data = json.loads(response.read())
        except ValueError:
            data = " "
        info["SyllabusNumber"] = "1002"
        info['Publisher'] = "NULL"
        try:
            info['Year'] = (data[0]['year'])
        except IndexError:
            info['Year'] = "NULL"
        try:

            info['Title'] = (data[0]['title'])
        except IndexError:
            info['Title'] = "NULL"

        try:
            dic['authors'] = (data[0]['fullCitation']).split("'")[0]
        except IndexError:
            dic['authors'] = "NULL"  # print dic

        try:
            x = (data[1]['fullCitation'])
        except IndexError:
            x = "NULL"
        try:
            journal = (between(x, '<i>', '</i>'))
        except IndexError:
            journal = "NULL"

        try:
            journal_page = after(x, "</i>").split(",")
        except IndexError:
            journal_page = "NULL"
        check = (get_authors(dic.values()))
        info['Author1Firstname'] = check[0].encode('ascii', 'ignore')
        info['Author1Lastname'] = check[2].encode('ascii', 'ignore')
        info['Author1Gender'] = check[1]
        info['Author1Probability'] = check[3]
        info['Author2Firstname'] = check[4].encode('ascii', 'ignore')
        info['Author2Lastname'] = check[6].encode('ascii', 'ignore')
        info['Author2Gender'] = check[5]
        info['Author2Probability'] = check[7]
        info['Author3Firstname'] = check[8].encode('ascii', 'ignore')
        info['Author3Lastname'] = check[10].encode('ascii', 'ignore')
        info['Author3Gender'] = check[9]
        info['Author3Probability'] = check[11]
        info['Author4Firstname'] = check[12].encode('ascii', 'ignore')
        info['Author4Lastname'] = check[14].encode('ascii', 'ignore')
        info['Author4Gender'] = check[13]
        info['Author4Probability'] = check[15]
        info['Author5Firstname'] = check[16].encode('ascii', 'ignore')
        info['Author5Lastname'] = check[18].encode('ascii', 'ignore')
        info['Author5Gender'] = check[17]
        info['Author5Probability'] = check[19]
        info['Journal'] = journal
        try:
            info['Volume'] = journal_page[-3]
        except IndexError:
            info['Volume'] = " "
        try:
            info['Number'] = journal_page[-2]
        except IndexError:
            info['Number'] = " "

        try:
            info['Pages'] = journal_page[-1]
        except IndexError:
            info['Pages'] = " "
        pprint(info)
        # time.sleep(5)

        with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
            json_text = json.dumps(info, indent=4)
            fp.write("{}\n".format(json_text))




def googleBooks(lst):
    for i in lst[:]:
        if len(i)>1:
            url = "https://www.googleapis.com/books/v1/volumes?q=" + i + "&maxResults=1&key=AIzaSyBADXkcoLOBG2UsddOpliFOq-JzEbbJ7_0"
            print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())

            info3["SyllabusNumber"]="xxxxxxx"
            try:

                info3['Publisher'] = (data['items'][0]['volumeInfo']['publisher'])
            except KeyError:
                info3['Publisher'] = " "
            except IndexError:
                info3['Publisher'] = " "

            try:
                info3['Year']= parser.parse(data['items'][0]['volumeInfo']['publishedDate']).year
            except ValueError:
                info3['Year']= " "
            except KeyError:
                info3['Year'] = " "

            try:
                dic1['author'] = (data['items'][0]['volumeInfo']['authors'])
            # except KeyError:
                # dic1['author'] = (data['items'][1]['volumeInfo']['authors'])
            except KeyError:
                dic1['author']= "NULL"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info['Pages'] = " "

            try:
                info3['Title'] = (data['items'][0]['volumeInfo']['title'])
            except KeyError:
                info3['Title']= "NULL"

            x= (dic1['author'])
            length = len(x)
            d = count - length
            if len(x) < count:
                try:
                    x.extend(["NULL"] * d)
                except AttributeError:
                    x=" "
            else:
                pass
            check= get_author_details(x)
            info3['Author1Firstname'] = check[0].encode('ascii', 'ignore')
            info3['Author1Lastname'] = check[2].encode('ascii', 'ignore')
            info3['Author1Gender'] = check[1]
            info3['Author1Probability']=check[3]
            info3['Author2Firstname'] = check[4].encode('ascii', 'ignore')
            info3['Author2Lastname'] = check[6].encode('ascii', 'ignore')
            info3['Author2Gender'] = check[5]
            info3['Author2Probability'] = check[7]
            info3['Author3Firstname'] = check[8].encode('ascii', 'ignore')
            info3['Author3Lastname'] = check[10].encode('ascii', 'ignore')
            info3['Author3Gender'] = check[9]
            info3['Author3Probability'] = check[11]
            info3['Author4Firstname'] = check[12].encode('ascii', 'ignore')
            info3['Author4Lastname'] = check[14].encode('ascii', 'ignore')
            info3['Author4Gender'] = check[13]
            info3['Author4Probability'] = check[15]
            info3['Author5Firstname'] = check[16].encode('ascii', 'ignore')
            info3['Author5Lastname'] = check[18].encode('ascii', 'ignore')
            info3['Author5Gender'] = check[17]
            info3['Author5Probability'] = check[19]
            info3['Journal']= "NULL"
            info3['Volume']= "NULL"
            info3['Number']="NULL"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info3['Pages'] ="NULL"
            pprint (info3)
            time.sleep(6)
            with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
                json_text = json.dumps(info3, indent=4)
                fp.write("{}\n".format(json_text))



def write2json(doc):
    with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
        json_text = json.dumps(doc, indent=4)
        fp.write("{}\n".format(json_text))


# write2json(extract_articles())
# print extract_articles()
# print extract_books()

# print extract_books1()
books= extract_books()
# print books
articles= extract_articles()
crossRef(articles)
googleBooks(books)


os.system("mongoimport --db sql2md --collection records2 --drop --file /Users/dipit/Documents/RA/RA/Demo/demo.json")