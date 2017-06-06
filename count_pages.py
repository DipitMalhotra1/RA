#-- coding: UTF-8 --

import re
import os
import pdfsplit
from pdfsplit import splitPages
rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
# print rxcountpages

def count_pages(filename):
    data = file(filename,"rb").read()
    return len(rxcountpages.findall(data))



pages= count_pages("/Users/dipit/Desktop/pdf/Mining.pdf")
print pages


import pdfx



# hard_code= "pdf2txt.py -O /Users/dipit/Desktop -o test1.html -t html -p " + str(pages) + " test1.pdf"

# print hard_code
os.chdir("/Users/dipit/Desktop/pdf")
# os.system(hard_code)

splitPages("/users/dipit/desktop/pdf/Mining.pdf", [slice(518, 536, None)])    # i.e. [0]