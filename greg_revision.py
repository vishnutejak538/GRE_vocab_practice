    """
     Revise all the greg mat words list. Pass the number of the set you want to revise as
     command line argument, will go through all 30 sets if none passed. 
     python greg_revision.py set_number
    """


import pickle
import sys

try:
    value = sys.argv[1]
except:
    value = "all"

with open("greg/greg_words.p",'rb') as file:
    load = pickle.load(file)

if value == "all":
    for i in range(1,31):
        for word in load["Group "+str(i)]:
            input(word)
else:
    for word in load["Group "+value]:
        input(word)