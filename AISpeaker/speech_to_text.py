import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'
r = sr.Recognizer()

with sr.Microphone() as source:
    print('듣고 있어요!')
    tts_ko = gTTS(text='듣고 있어요', lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)
    audio = r.listen(source)



try:
    text=r.recognize_google(audio, language="ko")
    print(text)
    tts_ko = gTTS(text=text, lang='ko')
    tts_ko.save(file_name)
    playsound(file_name)
except sr.UnknownValueError:
    print('인식 실패')
except sr.RequestError as e:
    print('Error: {0}'.format(e))

