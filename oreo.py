import pyttsx3  # need to install sepratly
import speech_recognition as sr  # need to install sepratly
import datetime
import os
import cv2  # need to install sepratly #pip install opencv-python
import random
from requests import get
import wikipedia # need to install sepratly
import webbrowser
import pywhatkit as kit # need to install sepratly


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice from text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please ")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am Ooreo sir ,please tell me how can i help you")


if __name__ == '__main__':
    wish()
    # while True:
    if 1:
        query = takecommand().lower()

        # logic building for task
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open browser" in query:
            npath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        #elif "ip address" in query:
        #    ip = get('https://ipify.org').text
        #    speak(f"your IP Address is {ip}")

        elif "wikipedia" in query:
            speak("serching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube"in query:
            speak("what should i serch on youtube")
            cm = takecommand().lower()
            print(cm)
            if cm == "nothing":
                webbrowser.open("www.youtube.com")
            else:
                kit.playonyt(f"{cm}")


        #Social Media
        elif "open facebook"in query:
            webbrowser.open("www.facebook.com")

        #elif "Stack overflow"in query:
            #webbrowser.open("www.stackoverflow.com")

        elif "open google"in query:
            speak("sir,what should i serch on google")
            cm = takecommand().lower()

            webbrowser.open(f"{cm}")

        #Sending whatsapp message

        #elif "send message" in query:
        #kit.sendwhatmsg("+91#numberhere","this is for testing protocol",2,25#time after 2 minuites)

        elif "play song on youtube" in query:
            speak("sir,wich song should i play")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")
        

