from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
#!/usr/bin/python
import MySQLdb


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="chom")        # name of the data base

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



def test(sql):

    cursor = db.cursor()
    try:

        cursor.execute(sql)

        db.commit()
    except:

        db.rollback()
    db.close()


def extract():
    string = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/sample.pdf")
    lines = list(filter(bool, string.split('1.')))
    Data = {}
    for i in lines:
        if 'References' in i:
            x = 'INSERT INTO `ref` (`Reference`) '
            'VALUES ({})'.format(i)
        test(x)


if __name__ == "__main__":
    hello_world_text = convert_pdf_to_txt("/Users/dipit/Documents/RA/RA/sample.pdf")
    # print(hello_world_text)
    extract()
    text_file = open("Output.txt", "w")
    text_file.write(hello_world_text)
    text_file.close()