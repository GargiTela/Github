import os
from gtts import gTTS
file = 'Hello. This is my first Natural language programming project of Text to speech recognization. Amazing experience. Glad to learn something new.'
language = 'en'
speech = gTTS(text = file, lang = language, slow = False).save('file.wav')
os.system('start file.wav')
