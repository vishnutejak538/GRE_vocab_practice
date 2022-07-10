# importing modules
import sys
import requests
from bs4 import BeautifulSoup

word = sys.argv[1]

# providing url
url = "https://wordsinasentence.com/"+word+"-in-a-sentence/"

# opening the url for reading

headers = {'Accept-Encoding': 'identity'}
r = requests.get(url, headers=headers)

# data = requests.get(url)

html = r.text

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')

text = []

# getting all the paragraphs
for para in htmlParse.find_all("p"):
    if para.get_text() != "":
        text.append(para.get_text().split(" 🔊")[0].strip())

# print(type(text[0]), text[5])

for i, sentence in enumerate(text):
    print(i,". ",sentence, end = "\n", sep="")