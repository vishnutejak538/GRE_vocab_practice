import pickle
from values import MAGOOSH_DICT

def get_meaning(word, words_deck):
    term = "meaning"
    keys = [key for key, _ in words_deck[word].items() if key[:-1] == term + '_']
    keys.reverse()
    if len(keys) != 0:
        for key in keys:
            print(key + ': ' + words_deck[word][key])  
try:
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
        i=0
        for k in words.keys():
            i+=1
            print(str(i)+". "+k+": ",end = " ")
            get_meaning(k,words)
            input()
        ch = input("Press enter to try another set, CTRL+C to exit. ")
        print()
        print()
except KeyboardInterrupt:
    print("Bye Bye ..! :)")