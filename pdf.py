from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
#!/usr/bin/python
import MySQLdb
import sqlite3

import os
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

def extract():
    string = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/sample.pdf")
    lines = list(filter(bool, string.split('.')))
    Data = {}
    for i in range(len(lines)):
        if 'References' in lines[i]:
            Data = (lines[i + 1])
            d = Data.split('  ')
            for r in range(4):
                x= "INSERT INTO Reference (NAME) \
                   VALUES" + '(' + '"{}"'.format(d[r]) + ')'
                data(x)


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
    hello_world_text = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/sample.pdf")
    extract()
    text_file = open("Output.txt", "w")
    text_file.write(hello_world_text)
    text_file.close()