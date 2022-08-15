"""
     Revise all the greg mat words list. Pass the number of the set you want to revise as
     command line argument, will go through all 30 sets if none passed. 
     python greg_revision.py set_number set_number2 set_numbern
"""


import pickle
import sys

unknows = []
if len(sys.argv) == 1:
    start = 1
    end = 30
else:
    start = sys.argv[1]
    end = sys.argv[2]

count = 1
with open("greg/greg_words.p",'rb') as file:
    load = pickle.load(file)
print("Selected sets: ", start," to ", end)

for i in range(int(start), int(end)+1):
    print("Set: ", i)
    for word in load["Group "+str(i)]:
        val = input(str(count)+". "+word)
        if val == "no":
            unknows.append(word)
        count+=1
    print("End of set: ", i, "\n\a")

if len(unknows) > 0:
    with open("unknows.txt", 'w') as file:
        file.write(str(unknows))
print("Number of unknown words: ", len(unknows), "\nTotal number of words: ", count)