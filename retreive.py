import pickle
import sys

def search_key(term, word):
    keys = [key for key, value in words[word].items() if key[:-1] == term + '_']
    if term == 'mnemonic':
        keys.reverse()
    # for key in words[word].items():
    #     print key
    # print words[word]
    # print keys
    if len(keys) != 0:
        for key in keys:
            print(key + ': ' + words[word][key])  # .encode('ascii', 'ignore')
            print()
            if term == 'meaning':
                try:
                    key2 = 'eg_' + key[-1]
                    input(key2 + ': ' + words[word][key2])  # .encode('ascii', 'ignore'))
                    print()
                except KeyError:
                    pass

                print()

        if term != 'meaning':
            input()
    else:
        # print 'No ' + term + 's for this word.'
        input('No ' + term + 's for this word. ')

if __name__ == "__main__":
    path = 'magoosh/Data/all_words.p'

    with open(path, 'rb') as handle:
        words = pickle.load(handle)
    print()

    try:
        word = sys.argv[1].strip()
    except:
        print("Usage: python retreive.py search_word")
        sys.exit(0)
    if word not in words:
        print("Word you are searching is not in this list :(")

    search_key('meaning', word)
    search_key('mnemonic', word)
    print()
