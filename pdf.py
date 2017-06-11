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

test= []
test1=[]
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

def quotes_name(r):

    quoted1 = re.compile('(.+)"[^"]+" ')
    quoted = re.compile('(.+)"[^"]+",')
    quoted2 = re.compile('(.+)"[^"]+".')

    for value in (quoted.findall(r) or quoted1.findall(r) or (quoted2.findall(r))):
        test1.append(value)
    # print len(test1)

    return test1[5:39]

def quotes(x):
    quoted = re.compile('"[^"]*"')
    for value in (quoted.findall(x)):
        l= len(value)
        if l>29:
            test.append(value)
    # print len(test)

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
    string = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/100021.pdf")
    # print string
    title = quotes(string)
    # print title
    # print "\n"
    name = quotes_name(string)
    removed = remove_numbers(name)
    pun=remove_numbers(removed)
    rem_punc= remove_punctuation(pun)
    # print "\n"
    zipped = zip(rem_punc, title)
    return zipped


if __name__ == "__main__":
    hello_world_text = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/test.pdf")
    extract()
    text_file = open("Output.txt", "w")
    text_file.write(hello_world_text)
    text_file.close()