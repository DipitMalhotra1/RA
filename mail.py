# # -- coding: UTF-8 --
#
# from pdf import convert_pdf_to_txt
# import re
# string=  convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/AmericanPolitics/13300003.pdf")
# # for i in string:
# # print re.findall(r'“([^"]*)”', i)
import os
from contextlib import contextmanager

import subprocess
from os import path
from glob import glob

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def find_ext(dr, ext):
    return glob(path.join("/Users/dipit/Documents/RA/RA/CitationsProjectAffiliates/Princeton","*.{}".format(ext)))

def get_pdf_html(lst):
    pdf = []
    html = []
    for i in lst:
        pdf.append(i.split("/")[-1])
    for i in pdf:
        html.append(i.split(".")[0] + ".html")
    return html
test= get_pdf_html(find_ext('.','pdf'))


def get_pdf_h(lst):
    pdf = []
    html = []
    for i in lst:
        pdf.append(i.split("/")[-1])
    for i in pdf:
        html.append(i.split(".")[0] + ".html")
    return pdf
test1= get_pdf_h(find_ext('.','pdf'))

os.chdir("/Users/dipit/Desktop/pdf/")
string= "pdf2txt.py -O /Users/dipit/Desktop/pdf/Book1-split.pdf  -o " + 'Book1-split.pdf' + " -t html " + 'Book1-split.pdf'
os.system(string)
