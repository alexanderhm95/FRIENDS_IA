from gtts import gTTS
from playsound import playsound
from os import *
import os

def texto_avoz(texto):
    tts = gTTS(text=texto, lang='es')
    tts.save(os.getcwd() +"\Audios\\"+"avoz.mp3")
    ruta=os.getcwd() +"\Audios\\"+"avoz.mp3"
    playsound(ruta)
    remove(ruta)   