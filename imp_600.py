# importing modules
import sys
import requests
from bs4 import BeautifulSoup
import pickle

# providing url
url = "https://brightlinkprep.com/all-the-600-gre-words-you-must-know/"

# opening the url for reading

headers = {'Accept-Encoding': 'identity'}
r = requests.get(url, headers=headers)

# data = requests.get(url)

html = r.text

# parsing the html file
htmlParse = BeautifulSoup(html, 'html.parser')
is_word = True
words_dict = {}
word = ''
# getting all the paragraphs
value = 1
for para in htmlParse.find_all("td"):
    if para.get_text() != "":
        if is_word:
            word  = para.get_text().strip()
            is_word = False
        else:
            if word in words_dict.keys():
                word = word+"_"+ str(value)
                value+=1
            else:
                value = 1
            words_dict[word] = para.get_text().strip()
            is_word = True

with open("600_words.p",'wb') as file:
    pickle.dump(words_dict,file)
