import RPi.GPIO as GPIO
import time
from src.config import config_obj

current_dist = 1000

def compute_live_distance():

    # global current_dist

    GPIO.setmode(GPIO.BOARD)

    TRIG = 31
    ECHO = 33

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    print("setup complete")

    try:
        for i in range(5000):
            GPIO.output(TRIG, False)
            time.sleep(1)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            while GPIO.input(ECHO)==GPIO.LOW:
                pulse_start = time.time()

            pulse_end=time.time()
            count = time.time()
            while GPIO.input(ECHO)==GPIO.HIGH and time.time()-count<0.1:
                pulse_end = time.time()
            
            pulse_duration = pulse_end - pulse_start
            distance = round(pulse_duration*17150,2)

            config_obj.current_distance = distance
            # current_dist = distance
            print(f"Distance: {distance} cm")
            time.sleep(2)

    except KeyboardInterrupt:
        # print("cleaning up")
        #GPIO.cleanup()
        raise IndexError("Stopping program after CTRL+C")
