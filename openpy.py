import subprocess
from os import path
from glob import glob
import os

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

def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]


def get_name(lst):
    for i in lst[:]:
        if i=='' or i==' ' or i=='  ' or len(i)==1:
            lst.remove(i)
    return lst

def italics2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200051/italics.txt', 'a') as f:
        f.write('{}'.format(data))


def quotes2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200051/quotes.txt', 'a') as f:
        f.write('{}'.format(data))

def plain2txt(data):
    with open ('/Users/dipit/Documents/RA/RA/Columbia/200071/titles.txt', 'a') as f:
        f.write('{}'.format(data))

rootdir = '/Users/dipit/Documents/RA/RA/CitationsProjectAffiliates'
x=[]
y=[]
def get_pdf_h(lst):
    pdf = []
    html = []
    for i in lst:
        pdf.append(i.split("/")[-1])
    for i in pdf:
        html.append(i.split(".")[0] + ".html")
    return pdf

def get_all_folder():
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
			x.append(os.path.join(subdir,file))
			y.append(os.path.join(subdir))
	return x[1:-1],y[1:-1]
folder= get_all_folder()