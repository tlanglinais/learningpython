# cmd run command: python .\rename.py samples/simple1.pdf
#!/usr/bin/env python

"""
Converts PDF text content (though not images containing text) to plain text, html, xml or "tags".
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# inputFile = 'SI 1143 Residual Report,01180206126-128,PINE_ISLAND_CHEMICAL,Halcon.pdf'
# outputFile = 'out.txt'

# Open a PDF file.
# inputFile = open('raw/SI 1143 Residual Report,01180206126-128,PINE_ISLAND_CHEMICAL,Halcon.pdf', 'rb')
inputFile = open('raw/simple1.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(inputFile)
print(parser)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
print(document)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
print(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
print(interpreter)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    print(interpreter.process_page(page))