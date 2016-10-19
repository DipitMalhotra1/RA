# -- coding: UTF-8 --

import urllib
import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdf import convert_pdf_to_txt
from openpy import get_name
import numpy as np
import openpyxl as pyxl
import string
import re
identity = string.maketrans("", "")
from openpy import between
author_names=[]
def get_from_txt():
	with open('output1.txt', 'r+') as fp:
		for i in fp:
			author_names.append(between(i,"fullCitation",", '"))
		return get_name(author_names)
t= get_from_txt()

def remove_spaces(string):
	y = [s.translate(identity, '0123456"789:\xc3-') for s in string]
	z = [s.translate(identity, "\xbc\xa9\xe2\x80\x90\x89\xa0\xb4\xa1") for s in y]

	return z
 
author=  get_name(remove_spaces(t))
def get_pdf():
	pdf = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/Berkeley/100021/100021.pdf")
	split_string= pdf.split("\n")
	titles=get_name(split_string)
	return titles	
tit= get_pdf()

def get_data(t):
	for i in t:
		url = "http://search.crossref.org/dois?q=" + i
		fp = urllib.urlopen(url)
		data = fp.read()
		d= data[0:200]
		with open('output1.txt', 'a') as outfile:
			print >> outfile, d

get_data(tit)
def data2excel(name):
	table = np.array([name])
	wb = pyxl.Workbook()
	ws = wb.active
	ws.title = 'Table 1'
	 
	tableshape = np.shape(table)
	alph = list(string.ascii_uppercase)
	 
	for i in range(tableshape[0]):
	    for j in range(tableshape[1]):
	        ws[alph[i]+str(j+1)] = table[i, j]
 
	wb.save('Scores.xlsx')
# print get_name(author)
# data2excel(author)