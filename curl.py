import os
import ast
from openpy import between
import string
import numpy as np
import openpyxl as pyxl
identity = string.maketrans("", "")
publisher = []
author = []
pages = []
title = []
booktitle = []
DOI = []
import csv
from openpy import get_name



def remove_spaces(string):
    y = [s.replace('": ', "", 1) for s in string]
    z = [s.replace('"', "", 1) for s in y]
    return z

def remove_paranthesis(y):
    remove_bib= [s.replace('Bibliography', "", 1) for s in y]
    remove_brackets= [s.translate(identity, "={}''=") for s in remove_bib]
    return remove_brackets


def get_from_txt():
    with open('output1.txt', 'r+') as fp:
        for i in fp:
            DOI.append(between(i, "doi", '",'))
        return DOI


t = get_from_txt()
do = remove_spaces(get_name(t))
# print do
# print do

work = ['http://dx.doi.org/10.1017/cbo9780511790416.014', 'http://dx.doi.org/10.1086/589891']


def split(lst):
    o = lst.split("\n")
    for i in o[:]:
        if i == "}":
            o.remove(i)
    return o


t = "Accept: application/x-bibtex"
doi = '"{}"'.format(t)
new = []


def get_results_doi(d):
    for i in d:
        query = "curl -LH " + doi + " " + str(i)
        result = os.popen(query).read()
        # pr split(result)
        new.append(split(result))
        # for i in split(result):
        #     new.append(i)
    return new


x= get_results_doi(do)
# print x

test1=[['@incollection{Aslund,', '\tdoi = {10.1017/cbo9780511790416.014},', '\turl = {http://dx.doi.org/10.1017/cbo9780511790416.014},', '\tpublisher = {Cambridge University Press ({CUP})},', '\tpages = {315--342},', '\tauthor = {Anders Aslund},', '\ttitle = {Bibliography},', '\tbooktitle = {How Capitalism Was Built}'], ['@article{Vogel_2008,', '\tdoi = {10.1086/589891},', '\turl = {http://dx.doi.org/10.1086/589891},', '\tyear = 2008,', '\tmonth = {jun},', '\tpublisher = {University of Chicago Press},', '\tvolume = {116},', '\tnumber = {3},', '\tpages = {423--466},', '\tauthor = {Jonathan Vogel},', '\ttitle = {Spatial Competition with Heterogeneous Firms},', '\tjournal = {Journal of Political Economy}'], ['@article{Labza__2014,', '\tdoi = {10.3917/afco.252.0189},', '\turl = {http://dx.doi.org/10.3917/afco.252.0189},', '\tyear = 2014,', '\tpublisher = {{CAIRN}},', '\tvolume = {252},', '\tnumber = {4},', '\tpages = {189},', "\tauthor = {Mehdi Labza{\\'{e}}},", '\ttitle = { Catherine Boone. Property and Political Order in Africa. Land Rights and the Structure of Politics },', '\tjournal = {Afrique contemporaine}'], ['@article{Portes_1996,', '\tdoi = {10.2307/2077169},', '\turl = {http://dx.doi.org/10.2307/2077169},', '\tyear = 1996,', '\tmonth = {mar},', '\tpublisher = {{SAGE} Publications},', '\tvolume = {25},', '\tnumber = {2},', '\tpages = {175},', '\tauthor = {Alejandro Portes and Peter Evans},', '\ttitle = {Embedded Autonomy: States and Industrial Transformation.},', '\tjournal = {Contemporary Sociology}'], ['@incollection{Beyer_2016,', '\tdoi = {10.1007/978-3-658-08184-3_38},', '\turl = {http://dx.doi.org/10.1007/978-3-658-08184-3_38},', '\tyear = 2016,', '\tmonth = {oct},', '\tpublisher = {Springer Nature},', '\tpages = {357--363},', '\tauthor = {J\xc3\xbcrgen Beyer},', '\ttitle = {Neil Fligstein: The Architecture of Markets},', '\tbooktitle = {Schl\xc3\xbcsselwerke der Wirtschaftssoziologie}']]

# print test1[1]



csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

def make_csv(lst):
    with open('mydata.csv', 'wb') as mycsvfile:
        writer = csv.DictWriter(mycsvfile,
                                fieldnames=["@", "DOI", "URL", "Year", "Month", "Publication", "Volume", "Number",
                                            "Pages", "Author", "Title", "BookTitle"], delimiter=',')
        writer.writeheader()
        thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
        for row in lst:
            thedatawriter.writerow(row)

make_csv(x)



