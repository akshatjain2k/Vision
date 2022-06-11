import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  #for taking voices
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!, Sir")

    else:
        speak("Good Evening!, Sir")

    speak("I am elli")
    speak('how may i help you')


def takeCommand():

    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:

        print("say that again please..")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'on youtube' in query:
            webbrowser.open(f"{query}\nhttps://www.youtube.com/")
            speak("Anything else, sir")
            

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("Your whatsapp is open in browser")
            speak("Anything else, sir")


        elif 'on gaana' in query:
            webbrowser.open(f"{query}\ngaana.com")
            speak("Anything else, sir")

        elif 'open google' in query:
            webbrowser.open(f"{query}\ngoogle.com")
            speak("Anything else, sir")

        elif 'open stackoverflow' in query:
            webbrowser.open(f"{query}\nhttps://stackoverflow.com/")
            speak("Anything else, sir")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\aksha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Anything else, sir")
        
        elif 'Run news API' in query:
            codePath = "C:\\Users\\aksha\\Desktop\\newsAPI.py"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(codePath)
            speak("Anything else, sir")

        elif 'can you hear me' in query:
            speak("yes Sir, perfectly")

        elif 'hi' in query:
            speak("hello Sir")

        elif 'no' in query:
            speak("Ok sir")
            break

        elif 'thank you' in query:
            speak("It is my duty, Sir")

        elif 'what is going on' in query:
            speak("Nothing intersting, sir")

        elif 'bye' in query:
            speak("bye bye sir, have a nice day")
            exit()



