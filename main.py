import os
import eel
from engine.features import *
from engine.command import *

def start():
    eel.init("www")

    speak("Booting System")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html',mode='chrome',host='localhost',block=True)