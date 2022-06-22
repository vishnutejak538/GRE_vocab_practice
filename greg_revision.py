"""
     Revise all the greg mat words list. Pass the number of the set you want to revise as
     command line argument, will go through all 30 sets if none passed. 
     python greg_revision.py set_number set_number2 set_numbern
"""


import pickle
import sys

values = sys.argv[1:]
if len(values) == 0:
    values = "all"
count = 1
with open("greg/greg_words.p",'rb') as file:
    load = pickle.load(file)
n = 0
if values == "all":
    values = list(range(1,31))
print("Selected sets: ", values)

for i in values:
    for word in load["Group "+str(i)]:
        val = input(str(count)+". "+word)
        if val == "no":
            n+=1
        count+=1
print("Number of unknown words: ", n, "\nTotal number of words: ", count)