import playsound
from gtts import gTTS  # google text to speech


def speak(text):
    tts = gTTS(text=text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


speak("Hello Mr.Durgesh Rai")
