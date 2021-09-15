import pickle
import os

for file in os.listdir(os.getcwd()):
    if file.endswith(".p"):
        with open(file,'rb') as word_file: 
            words = pickle.load(word_file)
            with open("set_texts/"+file.split(".")[0]+".txt",'w') as this_file:
                for word in words:
                    this_file.write(word+"\n")
            print("Completed ",file)