import pickle
from learn import search_key
import os
import sys
from values import MAGOOSH_DICT

while True:
    known = []
    unknown = []
    choice = input("Choose one: [1: common_words | 2: basic | 3: advanced]")
    deck = MAGOOSH_DICT[int(choice)]
    y = input('Enter roman numeral for deck: ')
    path = 'magoosh/Data/' + deck + y + '.p'

    with open(path, 'rb') as handle:
        words = pickle.load(handle)
    print()

    print(len(words))
    print("Press y and Enter if you know it or n if you don't know it: ")
    i=0
    for k in words.keys():
        # print k
        i+=1
        val = input("\t"+str(i)+". "+k+": ")
        if val == "":
            known.append(k)
        else:
            unknown.append(k)
            search_key('meaning', k,words)       
            search_key('mnemonic', k,words)

    if len(known) == len(words):
        print("Congrats you finished whole set :)")
        if os.path.exists("unknowns_"+deck+y+".txt"):
            os.remove("unknowns_"+deck + y+".txt")
    else:
        with open("unknowns_"+deck + y+".txt", 'w') as file:
            for word in unknown:
                file.write(word+", ")
    ch = input("Press enter to try another set, CTRL+C to exit. ")
    print()
    print()
