import requests
from src import audio_functions as af 
from src import movement as mvt
from threading import Thread
from src.config import config_obj as config_obj

URL = "http://192.168.2.12:5000"

t1 = Thread(target=mvt.approach())
t2 = Thread(target=af.sample_audio())
print(config_obj)

t1.start()

while True:
    if config_obj.movement_halted == True:
        t2.start()
        print(type(config_obj.audio_return_dict)) 
        wav_file = open("src/audio_sample.wav", "rb")
        requests.post(URL+"/process_audio", files={"file": wav_file}, json={"avgCoeff": config_obj.avg_initial_coeff})
        config_obj.movement_halted = False
