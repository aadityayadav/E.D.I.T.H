def weather():
    return "weather"

def music():
    print("this function will play music by calling the automated script")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def time():

    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

# elif 'play music' in query:
#             music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, songs[0]))

 #  elif 'the time' in query:
 #            strTime = datetime.datetime.now().strftime("%H:%M:%S")
 #            speak(f"Sir, the time is {strTime}")
 #
 # elif 'open code' in query:
 #            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
 #            os.startfile(codePath)
