# importing required modules
import PyPDF2
import sys


unknowns = []
try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except:
    print("PASS THE STARTING AND ENDING GROUP NUMBERS AS ARGUMENTS.")
    exit(0)

with open('gregmatlist32groups.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for page in range(start, end+1):
        pageObj = pdfReader.getPage(page-1)
        lines = pageObj.extractText().split("\n")
        print(lines[0])
        for l in lines[1:]:
            l = l.replace("\t"," ")
            if input(l) != "":
                unknowns.append(l)

if len(unknowns) > 0:
    with open("gregmat_unknowns.txt", 'a') as file:
        for line in unknowns:
            file.write(line+"\n")