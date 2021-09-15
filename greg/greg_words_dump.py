import csv
import pickle

data = csv.DictReader(open("greg_words_list.csv"))
words_dict = {}
for key in data.fieldnames:
    words_dict[key] = []
for row in data:
    for key in data.fieldnames:
        words_dict[key] += [row[key]]

with open("greg_words.p",'wb') as file:
    pickle.dump(words_dict,file)
