import wikipedia
import pyttsx3 as p

engine = p.init()
engine.setProperty('rate', 180)

def search_wiki(x):
    wik = wikipedia.page(x)
    print("")
    print(wik.title)
    print("")
    print("Get more information through this link: {}".format(wik.url))
    print("")
    content_search = wikipedia.summary(x,sentences=2)
    print(content_search)
    engine.say(content_search)
    engine.runAndWait()
