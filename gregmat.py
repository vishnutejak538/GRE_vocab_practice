"""
     Revise all the greg mat words list. Pass the number of the set you want to revise as
     command line argument, will go through all 30 sets if none passed. 
     python greg_revision.py set_number
"""


import csv
import sys

try:
    value = sys.argv[1]
except:
    value = "all"
count = 1
data = csv.DictReader(open("greg_words_list.csv"))

if value == "all":
    for key in data.fieldnames:
        data = csv.DictReader(open("greg_words_list.csv"))
        for row in data:
            input(str(count)+". "+row[key])
            count+=1
else:
    for row in data:
        input(str(count)+". "+row["Group "+value])
        count+=1