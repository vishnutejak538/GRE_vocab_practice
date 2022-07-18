# importing required modules
import PyPDF2
import sys


try:
    page = int(sys.argv[1])
except:
    print("PASS THE GROUP NUMBER AS ARGUMENT.")
    exit(0)

with open('gregmatlist32groups.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page-1)
    lines = pageObj.extractText().split("\n")
    print(lines[0])
    for l in lines[1:]:
        l = l.replace("\t"," ")
        input(l)

