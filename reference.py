string = convert_pdf_to_txt("/Users/dipit/Documents/RA/sample.pdf")
lines = list(filter(bool,string.split('\n')))
custData = {}
for i in range(len(lines)):
    if 'References' in lines[i]:
        custData['Name'] = lines[i+1]
print(custData)