from gtts import gTTS
from playsound import playsound
file_name = 'sample.mp3'

## 한글 문장
# text = '반갑다'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

playsound(file_name)