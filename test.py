import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
for voice in voices:
    print(voice.id)
    engine.setProperty('voice', voice.id)  #changing index, changes voices. o for male
    engine.say("Hello world!")
    engine.runAndWait()
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
