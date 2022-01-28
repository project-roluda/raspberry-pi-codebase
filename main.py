import requests
from src import audio_functions as af 
from src import movement as mvt
from src import live_distance as l_dst
from threading import Thread
from src.config import config_obj as config_obj

URL = "https://roluda-test-1.azurewebsites.net"
# URL = "http://192.168.2.12:5000"


# print("TESTING AZURE CONNECTION")
# print(requests.get(URL))

t1 = Thread(target=mvt.approach())
t2 = Thread(target=af.sample_audio())
t3 = Thread(target=l_dst.compute_live_distance())
print(config_obj)

t1.start()
t3.start()

while True:
    if config_obj.movement_halted == True:
        t2.start()
        print(type(config_obj.audio_return_dict)) 
        wav_file = open("src/audio_sample.wav", "rb")
        # headers = {"Content-Type":"application/json", "Accept":"text/plain"}
        resp =  requests.post(URL+"/process_audio", json={"avgCoeff":config_obj.avg_initial_coeff.tolist()})
        config_obj.movement_halted = False
        print(resp)
