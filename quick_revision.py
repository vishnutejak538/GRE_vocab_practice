import pickle
import os
import sys

def get_meaning(word, words_deck):
    term = "meaning"
    keys = [key for key, _ in words_deck[word].items() if key[:-1] == term + '_']
    keys.reverse()
    if len(keys) != 0:
        for key in keys:
            print(key + ': ' + words_deck[word][key])  

while True:
    known = []
    unknown = []
    if len(sys.argv) < 2:
        print("Usage: python revision.py deck_name")
        sys.exit(0)
    deck = sys.argv[1]
    deck = deck+"_"
    deck_list = ['common_words_', 'basic_', 'advanced_']
    if deck not in deck_list:
        sys.exit(0)
    # print(decks)

    y = input('Enter roman numeral for deck: ')
    path = 'magoosh/Data/' + deck + y + '.p'

    with open(path, 'rb') as handle:
        words = pickle.load(handle)
    print()

    print(len(words))
    i=0
    for k in words.keys():
        i+=1
        print(str(i)+". "+k+": ",end = " ")
        get_meaning(k,words)
        input()
    ch = input("Press enter to try another set, CTRL+C to exit. ")
    print()
    print()
