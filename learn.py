import pickle
import random



def search_key(term, word, words_deck):
    keys = [key for key, _ in words_deck[word].items() if key[:-1] == term + '_']
    keys.reverse()
    if len(keys) != 0:
        for key in keys:
            print(key + ': ' + words_deck[word][key])  

            if term == 'meaning':
                try:
                    key2 = 'eg_' + key[-1]
                    input(key2 + ': ' + words_deck[word][key2])  # .encode('ascii', 'ignore'))
                except KeyError:
                    pass

                print()

        if term != 'meaning':
            input()
    else:
        input('No ' + term + 's for this word. ')

if __name__ == "__main__":
    while True:

        decks = ['common_words_', 'basic_', 'advanced_']
        print(decks)

        x = input('Select one [1-3]: ')
        try:
            if int(x) < 1 or int(x) > 3:
                break
        except ValueError:
            break

        y = input('Enter roman numeral for deck: ')
        path = 'magoosh/Data/' + decks[int(x)-1] + y + '.p'

        with open(path, 'rb') as handle:
            words = pickle.load(handle)
        print()
        while True:
            freq = [0 for x in range(len(words))]
            all_words = [k for k,_ in words.items()]

            if sum(freq) >= 4*len(words):
                print('This deck is done. :)')
                print()
                print(freq)
                print()
                break
                
            ind = random.randint(0, len(words)-1)
            occ = 0

            while freq[ind]>3:
                ind = random.randint(0,len(words))
                occ += 1
                if occ > 100:
                    for ind in range(0,len(words)):
                        if freq[ind] < 4:
                            break

            freq[ind] += 1

            done = [ _ for _ in freq if _ == 4]
            seen = [ _ for _ in freq if _ != 0]

            word = all_words[ind]
            print(str(len(seen)) + ' words SEEN.   ' + str(len(done)) + ' words DONE.')
            print("\t"+word)
            input()

            search_key('meaning', word,words)   
            search_key('mnemonic', word,words)
            input('Press Enter to continue... ')

            print()
