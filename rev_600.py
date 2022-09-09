
import pickle
import sys

unknows = []
if len(sys.argv) == 2:
    start = 1
    end = int(sys.argv[1])
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

with open("600_words.p",'rb') as file:
    load = pickle.load(file)
print("Selected words: ", start," to ", end)

keys = list(load.keys())[start-1:end]
count = start

for i in keys:
        val = input(str(count)+". "+i+": ")
        val1 = input(load[i])
        if val != "" or val1 != "":
            unknows.append(i+": "+load[i])
        count+=1

if len(unknows) > 0:
    with open("unknows_600.txt", 'w') as file:
        for u in unknows:
            file.write(u)
print("Number of unknown words: ", len(unknows), "\nTotal number of words: ", count)