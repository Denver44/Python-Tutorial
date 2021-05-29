# ------------------------------------------------ DICTIONARY WITH THE VOICE ASSISTANT -----------------------------------------------------------

from gtts import gTTS  # google text to speech
import playsound

dict = {"consider": "deem to be",
        "minute": "small",
        "accord": "concurrence of opinion",
        "intend": "have in mind as a purpose",
        "chillax": "calm down and relax"}


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


word = input("Enter the Word of which u want meaning ")
speak(dict[word])
