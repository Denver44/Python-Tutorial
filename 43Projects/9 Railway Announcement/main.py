import pandas as pd
from gtts import gTTS
from pydub import AudioSegment


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename )


# This  Function returns pydubns audio segment
def mergeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)

    return combined


def genearteSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1-Genarting first Kripiya Dhyan Dijiye
    start = 88000  # 1.28 -> 88 second *1000 = 88000 milisecond
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 3-Genarting se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 5-Genarting ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 7-Genarting ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 9-Genarting kuch he smanay mai plaftfrom sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 11-Genarting pr aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-City
        textToSpeech(item['from'], '2_hindi.mp3')
        # 4 - Generate via-City
        textToSpeech(item['via'], '4_hindi.mp3')
        # 6 - Generate to-City
        textToSpeech(item['to'], '6_hindi.mp3')
        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')
        # 10 - Generate plaftfrom-Number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudio(audios)
        announcement.export(f'announcement_{index + 1}.mp3', format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton....")
    genearteSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement('announce_hindi.xlsx')
