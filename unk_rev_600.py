with open("unknows_600.txt", 'r') as file:
    data = file.readline()
    words = data.split(".")
    # print(words[0])
    for w in words:
        input(w)