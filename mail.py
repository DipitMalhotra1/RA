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

print test1
os.chdir("/Users/dipit/Desktop/pdf/")
string= "pdf2txt.py -O /Users/dipit/Desktop/pdf/Book1-split.pdf  -o " + 'Book1-split.pdf' + " -t html " + 'Book1-split.pdf'
os.system(string)
#
# for i in range(len(test1)):
#
#     string= "pdf2txt.py -O /Users/dipit/Desktop/pdf/Book1-split.pdf  -o " + (test[i]) + " -t html " +(test1[i])
#     # print string
#     # print os.getcwd()
#     os.chdir("/Users/dipit/Desktop/pdf/")
#     # print os.getcwd()
#     # with cd("/Users/dipit/Documents/RA/RA/Comparative"):
#     #     # we are in ~/Library
#     #     subprocess.call(string)
#
#
#     # os.system("cd /Users/dipit/Documents/RA/RA/Comparative")
#     os.system(string)