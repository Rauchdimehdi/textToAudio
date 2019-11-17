from gtts import gTTS

import os

Text= "Hello Everyone ! My name is Alexa."

language = 'en'

audio = gTTS(text= Text, lang= language, slow= False)

audio.save("intro.mp3")
