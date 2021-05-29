import pyttsx3  # text to speech recoginiton file.
import speech_recognition as sr
import datetime
import wikipedia  # to access the wikipedia
import webbrowser
import os
import smtplib  # Simple Mail Transfer Protocol

print("Initializing Jarvis")

MASTER = "DURGESH RAI"
# -----------(SAPI5) is the technology for voice recognition and synthesis provided by Microsoft---------#
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # this is for setting the voices


# function for the text to speech.
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    Minute = int(datetime.datetime.now().minute)
    sec = int(datetime.datetime.now().second)
    print(f"{hour}:{Minute}:{sec}")

    if hour >= 0 and hour < 6:
        speak("Its Midnight let's Creatimg something" + MASTER)
    elif hour >= 6 and hour < 12:
        speak("Good morning" + MASTER)
    elif hour >= 18 and hour <= 20:
        speak("Good Evening" + MASTER)
    elif hour >= 21 and hour <= 23:
        speak("Good Night" + MASTER)
    else:
        speak("take a rest buddy")
    # speak("How may I help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        print("listening done")

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        query = None
    return query


if __name__ == "__main__":
    speak("Hello I am Jarvis. Your Virtual Assistant")
    wishMe()
    while True:
        query = takecommand()
        # # logic
        if "wikipedia" in query.lower():
            speak("Searching wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query.lower():
            webbrowser.open("youtube.com")

        elif 'open google' in query.lower():
            webbrowser.open("google.com")

        elif 'open hackerrank' in query.lower():
            webbrowser.open("hackerrank.com")

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open sublime text editor' in query.lower():
            codepath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codepath)
