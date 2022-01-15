import RPi.GPIO as GPIO
import time

from src import throttle

GPIO.setmode(GPIO.BOARD)

# setup GPIO pins for servo motors
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

cm1 = GPIO.PWM(7, 15)
cm2 = GPIO.PWM(11, 15)
cm3 = GPIO.PWM(13, 15)
cm4 = GPIO.PWM(15, 15)

for i in range(1):
    throttle.throttle(cm1)
    throttle.throttle(cm2)
    throttle.throttle(cm3)
    throttle.throttle(cm4)

GPIO.cleanup()                                   
