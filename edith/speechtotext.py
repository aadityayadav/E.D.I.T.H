import speech_recognition as sr
import pyttsx3 as p
from web_automation import *
from wiki_search import *
from send_messages import *

sr.Microphone(device_index=1)

r = sr.Recognizer()
engine=p.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

with sr.Microphone() as source:

    engine.say("Hi, I hope you are doing well! ")
    # engine.runAndWait()

    # r.adjust_for_ambient_noise(source)
    # audio = r.listen(source)
    #
    #
    # try:
    #     recognised_text = r.recognize_google(audio)
    #     print(recognised_text)
    # except sr.UnknownValueError:
    #     engine.say("Could you please repeat yourself")
    # except sr.RequestError as e:
    #     engine.say("Error")

    engine.say("What would you like me to do?")
    engine.runAndWait()

    cont =""

    while cont!="quit now":

        r.adjust_for_ambient_noise(source)
        response = r.listen(source)

        try:
           print("")
           print("Listening...")
           recognised_text1 = r.recognize_google(response)
           print("Your Response:{}".format(recognised_text1))
           print("")
           recognised_text1= recognised_text1.lower()
           if recognised_text1 == "quit now":
               cont = "quit now"
           elif recognised_text1 == "play music":
               music()
           elif recognised_text1 == "send message":
                engine.say("Who do you want to send the message to?")
                engine.runAndWait()
                r.adjust_for_ambient_noise(source)
                contact_name = r.listen(source)
                try:
                     contact_name_char = r.recognize_google(contact_name)
                except sr.UnknownValueError:
                    engine.say("Could you please repeat yourself")
                except sr.RequestError as e:
                    engine.say("Error")
                engine.say("Who is the message content?")
                engine.runAndWait()
                msg_content = r.listen(source)
                try:
                     msg_content_char = r.recognize_google(msg_content)
                except sr.UnknownValueError:
                    engine.say("Could you please repeat yourself")
                except sr.RequestError as e:
                    engine.say("Error")
                send_msg(contact_name_char,msg_content_char)

           elif recognised_text1 == "search on wikipedia":
               engine.say("What do you want to search about?")
               engine.runAndWait()
               r.adjust_for_ambient_noise(source)
               search_req = r.listen(source)
               try:
                    search_req_char = r.recognize_google(search_req)
                    search_wiki(search_req_char)
               except sr.UnknownValueError:
                   engine.say("Could you please repeat yourself")
               except sr.RequestError as e:
                   engine.say("Error")
        except sr.UnknownValueError:
              engine.say("Could you please repeat yourself")
        except sr.RequestError as e:
              engine.say("Error")

    if cont == "quit now":
        engine.say("Okay quitting now")
        engine.runAndWait()
        exit("Edith over and out")


#
#
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

#
# import speech_recognition as sr
# r = sr.Recognizer()
# mic = sr.Microphone()
# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     transcript = r.recognize_google(audio)
#     print(transcript)


# import speech_recognition as sr
#
# # obtain audio from the microphone
# r = sr.Recognizer()
# d= ''
# while (d!='exit' and d!='quit'):
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)
#
# # recognize speech using Google Speech Recognition
#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         data = r.recognize_google(audio)
#         print("Google Speech Recognition thinks you said " + data)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))
#     d = data
