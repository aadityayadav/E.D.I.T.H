import pyttsx3 as p

engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 180)

engine.say("hello how are you doing")
engine.runAndWait()
