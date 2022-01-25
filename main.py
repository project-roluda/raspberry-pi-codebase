import requests
from src import audio_functions as af 
from src import movement as mvt
from threading import Thread
from src.config import config_obj as config_obj

t1 = Thread(target=mvt.approach())
t2 = Thread(target=af.sample_audio(3))
print(config_obj)

t1.start()

while True:
    if config_obj.movement_halted == True:
        data = t2.start()
        print(type(config_obj.audio_return_dict)) 
        config_obj.movement_halted = False
