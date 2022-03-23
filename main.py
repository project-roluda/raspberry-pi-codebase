from concurrent.futures import process
import requests
from src import audio_functions as af 
from src import movement as mvt
from src import live_distance as l_dst
from multiprocessing import Process
from threading import Thread
from src.config import config_obj as config_obj
import RPi.GPIO as GPIO
import time


URL = "https://roluda-test-v6.azurewebsites.net"
# URL = "http://192.168.2.12:5000"

current_dist = 100
# print("TESTING AZURE CONNECTION")
# print(requests.get(URL))

processes = []


def start_breathing():
    r = requests.get("https://roluda-test-v6.azurewebsites.net/respiration")

GPIO.cleanup()
    
while True:

    time.sleep(3)
    init_resp = requests.get(URL)
    json_resp_info = init_resp.json()
    print(json_resp_info)
    if json_resp_info["status"] == "standby":
#         GPIO.cleanup()

        t1 = Thread(target=mvt.approach)
        t2 = Thread(target=af.sample_audio)
        t3 = Thread(target=l_dst.compute_live_distance)
        print(config_obj)

        t1.start()
        t3.start()

        while True:
            print("main loop")
            print(config_obj.current_distance)
            time.sleep(1)
            if config_obj.current_distance < 5:
                config_obj.movement_halted=True
                print("config obj mvt halted is True")
            if config_obj.movement_halted == True:
                Thread(target=start_breathing).start()
                print("start audio recording")
                af.sample_audio()
                print(type(config_obj.audio_return_dict)) 
                wav_file = open("src/audio_sample.wav", "rb")
                # headers = {"Content-Type":"application/json", "Accept":"text/plain"}
                resp =  requests.post(URL+"/process_audio", json={"avgCoeff":config_obj.avg_initial_coeff.tolist()})
                config_obj.movement_halted = False
                print(resp)
            init_resp = requests.get(URL)
            json_resp_info = init_resp.json()
            if json_resp_info["status"] == "standby":
                break
