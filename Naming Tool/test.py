import PyPDF2
import os

# os.chdir('C:\\Users\\tsl\\OneDrive - Pine Island Chemical\\Programming\\Python\\Naming Tool')

pdfFileObj = open('test/test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
field = pdfReader.getFields(pageObj)
# print(field)
print(text)
# text.index('Halcon')
# text.index('Faye 2')
# text.index('Header Inj. HP-200ppm')
# text.index('2/8/2018')

#tomorrow
#write logic to create name

text = text.split('\n')
# Relevant Info
# 1. Type of Report - Index = 420
# 2. Customer - Index = 409
# 3. Location - Index = 430
# 4. Sample Point - Index = 405
# 5. Sample Date - Index = 400


pdfFileObj = open('test/test2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text2 = pageObj.extractText()
text2 = text2.split('\n')

# Relevant Info
# 1. Type of Report - Index = 421
# 2. Customer - Index = 410
# 3. Location - Index = 431
# 4. Sample Point - Index = 406
# 5. Sample Date - Index = 401

pdfFileObj = open('test/test3.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text3 = pageObj.extractText()
text3 = text3.split('\n')

# Relevant Info
# 1. Type of Report - Index = 420
# 2. Customer - Index = 409
# 3. Location - Index = 430
# 4. Sample Point - Index = 405
# 5. Sample Date - Index = 400