""" Pass the words you want to search as command line args """

# importing modules
import sys
from time import sleep
import requests
from bs4 import BeautifulSoup

def word_in_a_sentence(word:str):
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


if __name__ == '__main__':
    for i in sys.argv[1:]:
        print("Word: ", i)
        word_in_a_sentence(i)
        sleep(5)
