import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  #for taking voices
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Vision")
    speak('how may i help you sir')


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
        print(f"Boss said:{query}\n")
    except Exception as e:

        print("say that again please..")
        return 'None'
    return query


if __name__ == '__main__':
    wishme()
    takeCommand()
    while True:
        query = takeCommand().lower()

        #vlogic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            break

        elif 'play gaana' in query:
            webbrowser.open("https://gaana.com/")
            break

        elif 'open Google' in query:
            webbrowser.open("www.google.com")
            break

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            break

        # elif 'open mails' or 'check my mails' in query:
        #     webbrowser.open("https://mail.google.com/mail/u/0/")
        #     break

        elif 'open vs code' in query:
            codePath = "C:\\Users\\aksha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break

        elif 'hello' or 'hey' in query:
            speak('Hello Sir')

        elif 'thank you' in query:
            speak('It is my duty, Sir')

        elif 'open Instagram' in query:
            speak('your instagram will be open in few second')
            print('Please wait...')

        elif 'bye' in query:
            speak('bye sir, have a nice day')
            exit()

