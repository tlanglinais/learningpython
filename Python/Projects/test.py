import PyPDF2

pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
text = pageObj.extractText()

text.index('Halcon')
text.index('Faye 2')
text.index('Header Inj. HP-200ppm')
text.index('2/8/2018')