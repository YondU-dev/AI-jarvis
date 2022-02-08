import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random
import requests
from bs4 import BeautifulSoup

from wikipedia.wikipedia import random, search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class Recognizer(sr.AudioSource):
            def __init__(self):
                  self.energy_threshold = 500
                  self.pause_threshold = 0.8


def wishMe():
    speak("Hello , ")

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 17:
            speak("Good afternoon")

    elif hour >= 17 and hour < 20:
        speak("Good Evening")

    else:
        speak("Good Night")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what is it")
        print("what is it")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Please say that again")
        print("Please say that again")
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Finding')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wiki")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open chunkbase' in query:
            webbrowser.open('chunkbase.com')

        elif 'open gmail' in query:
            webbrowser.open('gmail.com')

        elif 'open Disney Plus' in query:
            webbrowser.open('www.hotstar.com')
            speak("Opening Diseny plus")

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open wikipedia' in query:
            webbrowser.open('wikipedia.org')

        elif 'open translate' in query:
            webbrowser.open('translate.google.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open minecraft' in query:
            codePath = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"
            os.startfile(codePath)
            speak("Opening Minecraft Launcher")


        elif 'open Epic games' in query:
            codePath = "E:\\Yondu\\Epic Games\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codePath)
            speak("Opening Epic Games")

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            speak("Opening Chrome")

        elif 'open o b s' in query:
            codePath = "C:\\Program Files\\obs-studio\\bin\64bit\\obs64.exe"
            os.startfile(codePath)
            speak("Opening OBS Studio")

        elif 'open audacity' in query:
            codePath = "E:\\Yondu\\Audacity\\Audacity\\audacity.exe"
            os.startfile(codePath)
            speak("Opening Audacity")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Minecraft Launcher")

        elif 'open filmora' in query:
            codePath = "E:\\Yondu\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(codePath)
            speak("Opening Minecraft Launcher")
            

        elif 'email to me' in query:
            try:
                speak("what is the text ?")
                content = takeCommand()
                to = 'sanketnarvekar1995@gmail.com'
                sendEmail(to, content)
                speak("Your mail has been sent")
            except Exception as e:
                print(e)
                speak("There a problem sending your mail")

        elif 'you are right' in query:
            speak(f"I know thank you")

        elif 'hai' in query:
            speak(f"hello how are you")

        elif 'how are you' in query:
            speak(f"I am fine, Whats about you")

        elif 'i am fine' in query:
            speak(f"Thats good")

        elif 'who are you' in query:
            speak(f"I am Friday")

        elif 'who is your favourite Avenger' in query:
            speak(f"All avengers are my favorite, but i like Spider man, iron man and thor the most")

        elif 'emergency contacts' in query:
            speak(f"")

        elif 'hello' in query:
            speak(f"hello, how are you")

        elif 'where are you' in query:
            speak(f"I am in your device")

        elif 'sing a song' in query:
            speak(f"When you feel it’s hopeless When you think that you lost, Oh I will take your hand andWe‘ll rise up from the dust, Oh")

        elif 'whats my name' in query:
            speak(f"I told me your name is moms")

        elif 'what is your age ' in query:
            speak(f"I dont have age , i am immortal")

        elif 'your age' in query:
            speak(f"I dont have age , i am immortal")

        elif 'hello' in query:
            speak(f"hello, how are you")
        
        elif 'play song' in query:
            music_dir = 'E:\\Yondu\YT channel\\video content\\Recordings\\.Edit content\\Trial music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        