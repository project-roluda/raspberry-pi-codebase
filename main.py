from concurrent.futures import process
import requests
from src import audio_functions as af 
from src import movement as mvt
from src import live_distance as l_dst
from multiprocessing import Process
from src.config import config_obj as config_obj
import time

from src.live_distance import current_dist

URL = "https://roluda-test-1.azurewebsites.net"
# URL = "http://192.168.2.12:5000"


# print("TESTING AZURE CONNECTION")
# print(requests.get(URL))

processes = []


t1 = Process(target=mvt.approach)
t2 = Process(target=af.sample_audio)
t3 = Process(target=l_dst.compute_live_distance)
print(config_obj)

t1.start()
t3.start()

while True:
    print(current_dist)
    if config_obj.current_distance < 5:
        config_obj.movement_halted=True
        print("config obj mvt halted is True")
    if config_obj.movement_halted == True:
        print("start audio recording")
        af.sample_audio()
        print(type(config_obj.audio_return_dict)) 
        wav_file = open("src/audio_sample.wav", "rb")
        # headers = {"Content-Type":"application/json", "Accept":"text/plain"}
        resp =  requests.post(URL+"/process_audio", json={"avgCoeff":config_obj.avg_initial_coeff.tolist()})
        config_obj.movement_halted = False
        print(resp)
