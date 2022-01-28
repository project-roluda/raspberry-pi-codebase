import RPi.GPIO as GPIO
import time
from src.config import config_obj

from src import throttle

GPIO.setmode(GPIO.BOARD)

# setup GPIO pins for servo motors
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

cm1 = GPIO.PWM(7, 50)
cm2 = GPIO.PWM(11, 50)
cm3 = GPIO.PWM(13, 50)
cm4 = GPIO.PWM(15, 50)
cm5 = GPIO.PWM(16, 50)


def approach():

    start = time.time()

    cm1.start(0)
    cm2.start(0)
    cm3.start(0)
    cm4.start(0)
    cm5.start(0)

    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(16, True)

    cm1.ChangeDutyCycle(8)
    cm2.ChangeDutyCycle(8)
    cm3.ChangeDutyCycle(8)
    cm4.ChangeDutyCycle(8)
    cm5.ChangeDutyCycle(8)
    time.sleep(1)

    cm1.ChangeDutyCycle(6)
    cm2.ChangeDutyCycle(6)
    cm3.ChangeDutyCycle(6)
    cm4.ChangeDutyCycle(6)
    cm5.ChangeDutyCycle(6)
    time.sleep(1)


    
    cm1.ChangeDutyCycle(7)
    cm2.ChangeDutyCycle(7)
    cm3.ChangeDutyCycle(7)
    cm4.ChangeDutyCycle(7)
    cm5.ChangeDutyCycle(7)

    print(config_obj.movement_halted)

    # cm1.stop()
    # cm2.stop()
    # cm3.stop()
    # cm4.stop()
    # cm5.stop()
    print("stop()")
    GPIO.cleanup()                                   
