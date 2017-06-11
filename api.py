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
joinbook = []
test2 = []
gender=[]
write_list=[]
first_name=[]
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

def googleBooks(lst):
    for i in lst[:]:
        if len(i)>1:
            url = "https://www.googleapis.com/books/v1/volumes?q=" + i + "&maxResults=1&key=AIzaSyBADXkcoLOBG2UsddOpliFOq-JzEbbJ7_0"
            print url
            response = urllib.urlopen(url)
            data = json.loads(response.read())
            try:
                info3['URL'] = (data['items'][0]['volumeInfo']['previewLink'])
            except KeyError:
                info['URL']= 'No Url Available'
            try:
                info3['Description'] = (data['items'][0]['volumeInfo']['description'])
            except KeyError:
                info['Description']= 'Not Available'

            try:
                info3['ISBN'] = (data['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'])
            except KeyError:
                info['Description']= 'Not Available'
            try:

                info3['Publisher'] = (data['items'][0]['volumeInfo']['publisher'])
            except KeyError:
                info3['Publisher'] = "Not Available"
            except IndexError:
                info3['Publisher'] = "Not Available"

            try:
                info3['Year']= parser.parse(data['items'][0]['volumeInfo']['publishedDate']).year
            except ValueError:
                info3['Year']= "Not Available"
            except KeyError:
                info3['Year'] = "Not Available"

            try:
                dic1['author'] = (data['items'][0]['volumeInfo']['authors'])
            # except KeyError:
                # dic1['author'] = (data['items'][1]['volumeInfo']['authors'])
            except KeyError:
                dic1['author']= "Not Available"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info['Pages'] = "Not Available"

            try:
                info3['Title'] = (data['items'][0]['volumeInfo']['title'])
            except KeyError:
                info3['Title']= "Not Available"

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
            info3['Journal']= "Not Available"
            info3['Volume']= "Not Available"
            info3['Number']="Not Available"
            try:
                info3['Pages'] = (data['items'][0]['volumeInfo']['pageCount'])
            except KeyError:
                info3['Pages'] ="Not Available"
            pprint (info3)
            time.sleep(6)
            with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
                json_text = json.dumps(info3, indent=4)
                fp.write("{}\n".format(json_text))


def crossRef(lst):
    i=0
    for i in lst:
        url = "https://api.crossref.org/works?query=" + i + "&rows=2"
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
        # pprint (data['message']['items'][0])
        try:
            info['DOI'] = 'http://dx.doi.org/'+ (data['message']['items'][0]['DOI'])
        except KeyError:
            info['DOI'] = 'Unavailable'

        try:
            info['ISSN']= (data['message']['items'][0]['ISSN'])
        except KeyError:
            info['ISSN'] = 'Unavailable'
        try:

            info['Author1Lastname']= (data['message']['items'][0]['author'][0]['family'])
        except KeyError:
            info['Author1Lastname'] = 'NULL'
        try:
            info['Author1Firstname']=(data['message']['items'][0]['author'][0]['given']).split(' ')[0]

        except KeyError:
            info['Author1Firstname']='NULL'

        try:
            info['Author2Firstname'] = (data['message']['items'][0]['author'][1]['given'])

        except KeyError:
            info['Author2Firstname'] = 'NULL'
        except IndexError:
            info['Author2Firstname'] = 'NULL'

        try:
            info['Author2Lastname']= (data['message']['items'][0]['author'][1]['family'])
        except KeyError:
            info['Author2Lastname'] = 'NULL'
        except IndexError:
            info['Author2Lasttname'] = 'NULL'


        try:
            info['Author3Firstname'] = (data['message']['items'][0]['author'][2]['given'])

        except KeyError:
            info['Author3Firstname'] = 'NULL'
        except IndexError:
            info['Author3Firstname'] = 'NULL'

        try:
            info['Author3Lastname']= (data['message']['items'][0]['author'][2]['family'])
        except KeyError:
            info['Author3Lastname'] = 'NULL'
        except IndexError:
            info['Author3Lasttname'] = 'NULL'

        try:
            info['Author4Firstname'] = (data['message']['items'][0]['author'][3]['given'])

        except KeyError:
            info['Author4Firstname'] = 'NULL'
        except IndexError:
            info['Author4Firstname'] = 'NULL'

        try:
            info['Author4Lastname'] = (data['message']['items'][0]['author'][3]['family'])
        except KeyError:
            info['Author4Lastname'] = 'NULL'
        except IndexError:
            info['Author4Lasttname'] = 'NULL'

        try:
            info['Author5Firstname'] = (data['message']['items'][0]['author'][4]['given'])

        except KeyError:
            info['Author5Firstname'] = 'NULL'
        except IndexError:
            info['Author5Firstname'] = 'NULL'

        try:
            info['Author5Lastname'] = (data['message']['items'][0]['author'][4]['family'])
        except KeyError:
            info['Author5Lastname'] = 'NULL'
        except IndexError:
            info['Author5Lasttname'] = 'NULL'


        try:
            info['Cited by'] = (data['message']['items'][0]['is-referenced-by-count'])
        except KeyError:
            info['Cited by'] ='Unavailable'

        try:
            info['Issue']=(data['message']['items'][0]['issue'])
        except KeyError:
            info['Issue']='Unavailable'

        try:
            info['Page'] = (data['message']['items'][0]['page'])
        except KeyError:
            info['Page'] = 'Unavailable'

        try:
            info['Publisher'] = (data['message']['items'][0]['publisher'])
        except KeyError:
            info['Publisher'] = 'Unavailable'

        try:
            info['Title'] = (data['message']['items'][0]['title'])
        except KeyError:
            info['Title'] = 'Unavailable'

        try:
            info['Type'] = (data['message']['items'][0]['type'])
        except KeyError:
            info['Type'] = 'Unavailable'

        try:
            info['Volume'] = (data['message']['items'][0]['volume'])
        except KeyError:
            info['Volume'] = 'Unavailable'

        # print list(info)
        # first_name = list(info.values())
        first_name.extend([info.get('Author1Firstname'),info.get('Author2Firstname'),info.get('Author3Firstname'),info.get('Author4Firstname'),info.get('Author5Firstname')])
        for i in  range(1,len(get_author_details(first_name)),2):
            gender.append(get_author_details(first_name)[i])

        info['Author1Gender']= gender[0]
        info['Author2Gender']=gender[2]
        info['Author3Gender'] = gender[4]
        info['Author4Gender'] = gender[6]
        info['Author5Gender'] = gender[8]
        info['Author1Probability']= gender[1]
        info['Author2Probability']= gender[3]
        info['Author3Probability']= gender[5]
        info['Author4Probability']= gender[7]
        info['Author5Probability']= gender[9]




        pprint (info)
        with open('/Users/dipit/Documents/RA/RA/Demo/demo.json', 'a') as fp:
            json_text = json.dumps(info, indent=4)
            fp.write("{}\n".format(json_text))








books= extract_books()
googleBooks(books)
articles= extract_articles()
crossRef(articles)
os.system("mongoimport --db sql2md --collection records2 --drop --file /Users/dipit/Documents/RA/RA/Demo/demo.json")