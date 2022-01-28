from concurrent.futures import process
import requests
from src import audio_functions as af 
from src import movement as mvt
from src import live_distance as l_dst
from multiprocessing import Process
from src.config import config_obj as config_obj
import time
import RPi.GPIO as GPIO


URL = "https://roluda-test-1.azurewebsites.net"
# URL = "http://192.168.2.12:5000"

current_dist = 100

def compute_live_distance():


    GPIO.setmode(GPIO.BOARD)

    TRIG = 31
    ECHO = 33

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    print("setup complete")

    try:
        while True:
            GPIO.output(TRIG, False)
            time.sleep(1)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
            
            pulse_duration = pulse_end - pulse_start
            distance = round(pulse_duration*17150,2)

            global current_dist
            current_dist = distance
            print(f"Distance: {distance} cm")
            time.sleep(2)

    except KeyboardInterrupt:
        print("cleaning up")
        GPIO.cleanup()
        raise IndexError("Stopping program after CTRL+C")


# print("TESTING AZURE CONNECTION")
# print(requests.get(URL))

processes = []


t1 = Process(target=mvt.approach)
t2 = Process(target=af.sample_audio)
t3 = Process(target=compute_live_distance)
print(config_obj)

t1.start()
t3.start()

while True:
    print(f"current_dist {current_dist}")
    time.sleep(3)
    if current_dist < 5:
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
