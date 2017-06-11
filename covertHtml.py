# # -- coding: UTF-8 --
import urllib, json
import os
import glob
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
import sys
from nltk.corpus import names
from gp import get_gender
import random
reload(sys)

from utility import *
from pdfsplit import splitPages
from itertools import islice
file=[]
bTags=[]
page=[]
a=[]
fTags=[]
z=[]
new=[]
info={}
dic1={}
joinbook=[]
test2=[]
info3={}
rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
def count_pages(filename):
    data = file(filename,"rb").read()
    return len(rxcountpages.findall(data))
def get_pages(pdf):
    with open(pdf) as f:
        for line in f:
            if 'Page' in line:
                a.append(''.join(islice(f, 100)))
        for i in range(len(a)):
            if "References" in a[i] or 'REFERENCES' in a[i] or 'EFERENCES' in a[i]:
                return i
# print get_pages("/Users/dipit/Documents/RA/RA/Docs/PDF/Dimensional.pdf.html")
# print get_pages("/Users/dipit/Documents/RA/RA/Docs/PDF/sample.pdf.html")

def extract_articles():
    for i in soup.find_all('span', style=lambda x: x and 'Regu;' in x):
        fTags.append(i.text)
    for i in soup.find_all('span', style=lambda x: x and 'Antiqua;' in x):
        fTags.append(i.text)
    for i in soup.find_all('span', style=lambda x: x and 'Times-Roman;' in x):
        fTags.append(i.text)

    fTags1=[item.encode('utf-8') for item in fTags]
    fTags1=[item.replace('\n','') for item in fTags1]

    # print fTags1
    print "\n\n"
    for previous, item, nxt in previous_and_next(fTags1):
        try:
            if item[-1]=='\n':
                try:
                    z.append(''.join(item,next))
                except TypeError:
                    pass
        except IndexError:
            pass
        z.append(item)
    # print z
    for i in range(len(z)):
        new.extend(re.findall("\“(.+)\”", z[i]))

    return new
# print extract_articles()

def extract_books1():
    result=[]

    # for i in soup.find_all('span', style=lambda x: x):    #if column wise cited#
    for i in soup.find_all('span', style=lambda x: x):

        bTags.append(i.text)
    filtered = filter(None, bTags)
    filtered=[x.strip() for x in filtered if x.strip()]
    filtered=[item.replace('\n','') for item in filtered]

    print filtered
    print"\n\n"

    for previous,item,nxt in previous_and_next(filtered):
        if item[-1]==',':
            try:
                joinbook.append (''.join(item + nxt))
            except TypeError:
                pass

    for i in range(len(joinbook)):
        # test2.extend(re.findall(",\s*([^,]+)$", joinbook[i]))
        test2.extend(re.findall("\,.*", joinbook[i]))

    test3=[x for x in test2 if not any(c.isdigit() for c in x)]
    test3=[x for x in test3 if '“' not in x]

    return test3



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
        info['URL']= data[0]['doi']
        info['Publisher'] = "Not Available"
        try:
            info['Year'] = (data[0]['year'])
        except IndexError:
            info['Year'] = "Not Available"
        try:

            info['Title'] = (data[0]['title'])
        except IndexError:
            info['Title'] = "Not Available"

        try:
            dic['authors'] = (data[0]['fullCitation']).split("'")[0]
        except IndexError:
            dic['authors'] = "Not Available"  # print dic

        try:
            x = (data[1]['fullCitation'])
        except IndexError:
            x = "Not Available"
        try:
            journal = (between(x, '<i>', '</i>'))
        except IndexError:
            journal = "Not Available"

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
            info['Volume'] = "Not Available"
        try:
            info['Number'] = journal_page[-2]
        except IndexError:
            info['Number'] = "Not Available"

        try:
            info['Pages'] = journal_page[-1]
        except IndexError:
            info['Pages'] = "Not Available"
        pprint(info)
        # time.sleep(5)

        with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
            json_text = json.dumps(info, indent=4)
            fp.write("{}\n".format(json_text))

def googleBooks(lst):
    for i in lst[:]:
        if len(i) > 1:
            url = "https://www.googleapis.com/books/v1/volumes?q=" + i + "&maxResults=1&key=AIzaSyBADXkcoLOBG2UsddOpliFOq-JzEbbJ7_0"
            print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())
            try:
                info3['URL'] = (data['items'][0]['volumeInfo']['previewLink'])
            except KeyError:
                info['URL'] = 'No Url Available'
            try:
                info3['Description'] = (data['items'][0]['volumeInfo']['description'])
            except KeyError:
                info['Description'] = 'Not Available'

            try:
                info3['ISBN'] = (data['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'])
            except KeyError:
                info['Description'] = 'Not Available'
            try:

                info3['Publisher'] = (data['items'][0]['volumeInfo']['publisher'])
            except KeyError:
                info3['Publisher'] = "Not Available"
            except IndexError:
                info3['Publisher'] = "Not Available"

            try:
                info3['Year'] = parser.parse(data['items'][0]['volumeInfo']['publishedDate']).year
            except ValueError:
                info3['Year'] = "Not Available"
            except KeyError:
                info3['Year'] = "Not Available"

            try:
                dic1['author'] = (data['items'][0]['volumeInfo']['authors'])
                # except KeyError:
                # dic1['author'] = (data['items'][1]['volumeInfo']['authors'])
            except KeyError:
                dic1['author'] = "Not Available"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info['Pages'] = "Not Available"

            try:
                info3['Title'] = (data['items'][0]['volumeInfo']['title'])
            except KeyError:
                info3['Title'] = "Not Available"

            x = (dic1['author'])
            length = len(x)
            d = count - length
            if len(x) < count:
                try:
                    x.extend(["NULL"] * d)
                except AttributeError:
                    x = " "
            else:
                pass
            check = get_author_details(x)
            info3['Author1Firstname'] = check[0].encode('ascii', 'ignore')
            info3['Author1Lastname'] = check[2].encode('ascii', 'ignore')
            info3['Author1Gender'] = check[1]
            info3['Author1Probability'] = check[3]
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
            info3['Journal'] = "Not Available"
            info3['Volume'] = "Not Available"
            info3['Number'] = "Not Available"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info3['Pages'] = "Not Available"
            pprint(info3)
            time.sleep(6)
            with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
                json_text = json.dumps(info3, indent=4)
                fp.write("{}\n".format(json_text))




path= os.path.dirname(os.getcwd()+"/Docs")


for i in traverse(os.path.dirname(os.getcwd()) + "/RA/Docs/PDF"):

    soup = BeautifulSoup(open(i))
    crossRef(extract_articles())
    googleBooks(extract_books1())


#
# splitPages("/Users/dipit/Documents/RA/RA/Docs/sample.pdf", [slice(get_pages("/Users/dipit/Documents/RA/RA/Docs/sample.html"),count_pages("/Users/dipit/Documents/RA/RA/Dimensional.pdf"), None)])    # i.e. [0]

# os.system("pdf2txt.py -O /Users/dipit/Documents/RA/RA/ -o IEEE-split.html /Users/dipit/Documents/RA/RA/sample.pdf")