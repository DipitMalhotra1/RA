# -- coding: UTF-8 --
import nltk
from nameparser.parser import HumanName
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
#!/usr/bin/python
# import MySQLdb
import sqlite3
import re
import string
import os
identity = string.maketrans("", "")

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

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

test= []
test1=[]
def quotes_name(r):

    quoted1 = re.compile('(.+)"[^"]+" ')
    quoted = re.compile('(.+)"[^"]+",')
    quoted2 = re.compile('(.+)"[^"]+".')



    for value in (quoted.findall(r) or quoted1.findall(r) or (quoted2.findall(r))):
        test1.append(value)
    print len(test1)

    return test1[5:39]

def quotes(x):
    quoted = re.compile('"[^"]*"')
    for value in (quoted.findall(x)):
        l= len(value)
        if l>29:
            test.append(value)
    print len(test)

    return test[4:38]
        # print len(test)


def remove_punctuation(result):
    #
    r = [''.join(x for x in par if x not in string.punctuation) for par in result]
    # rem_numbers= [''.join([i for i in r if not i.isdigit()])]
    return r

def remove_numbers(string):
    y = [s.translate(identity, "0123456789") for s in string]
    z =  [s.translate(identity, "\xe2\x80\xa2") for s in y]
    return z

def extract():
    string = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/test.pdf")
    # print string
    title = quotes(string)
    print title
    print "\n"
    name = quotes_name(string)
    removed = remove_numbers(name)
    pun=remove_numbers(removed)
    print remove_punctuation(pun);
    print "\n"


    zipped = zip(removed, title)
    print zipped
    print len(zipped)
    #
    # for i in range(len(zipped)):
    #
    #     scholar = "python scholar.py -c 1 --author " + (zipped[i][0]) + "--phrase  " + zipped[i][1]
    #     print scholar
    # # os.system(scholar)









    # lines = list(filter(bool, string.split('"')))
    # Data = {}
    # for i in range(len(lines)):
    #     if 'References' in lines[i]:
    #         Data = (lines[i + 1])
    #         d = Data.split('  ')
    #         names = get_human_names(str(d))
    #         print d
    #         print "LAST, FIRST"
    #         for name in names:
    #             last_first = HumanName(name).last + ', ' + HumanName(name).first
    #             print last_first
    #
    #         for r in range(4):
    #             x= "INSERT INTO Reference (NAME) \
    #                VALUES" + '(' + '"{}"'.format(d[r]) + ')'
    #             data(x)


def data(sql):
    conn = sqlite3.connect('test2.db', timeout=100)
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO Reference(NAME) \
    #                    VALUES ('dipit')")

    cursor.execute(sql)
    p = cursor.execute("Select * from Reference Limit 1")
    for row in p:
        x = "python scholar.py -c 1 --author " + row[0]
        print(x)
        os.system(x)

    conn.commit()
    # print("Records created successfully")
    conn.close()

if __name__ == "__main__":
    hello_world_text = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/test.pdf")
    extract()
    text_file = open("Output.txt", "w")
    text_file.write(hello_world_text)
    text_file.close()