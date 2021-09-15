import os
import pickle

all_words_dict = {}
for file_name in os.listdir(os.getcwd()):
    if not file_name.__contains__(".py"):
        print("Currently on ",file_name)
        with open(file_name,'rb') as file:
            data = pickle.load(file)
            all_words_dict.update(data)
print("Completed!..")
print(len(all_words_dict))
pickle.dump(all_words_dict,open("all_words.p",'wb'))