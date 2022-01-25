import RPi.GPIO as GPIO
import time

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
cm6 = GPIO.PWM(18, 50)

#for i in range(1):
    #throttle.throttle(cm1, 20)
#    throttle.throttle(cm2)
#    throttle.throttle(cm3)
#    throttle.throttle(cm4)

#throttle.rotateAngle(cm1, 10)

start = time.time()

cm1.start(0)
cm2.start(0)
cm3.start(0)
cm4.start(0)
cm5.start(0)
cm6.start(0)

GPIO.output(7, True)
GPIO.output(11, True)
GPIO.output(13, True)
GPIO.output(15, True)
GPIO.output(16, True)
GPIO.output(18, True)

cm1.ChangeDutyCycle(7.3)
cm2.ChangeDutyCycle(7.3)
cm3.ChangeDutyCycle(7.3)
cm4.ChangeDutyCycle(7.3)
cm5.ChangeDutyCycle(7.3)
cm6.ChangeDutyCycle(7.3)

time.sleep(1)

cm1.ChangeDutyCycle(6.7)
cm2.ChangeDutyCycle(6.7)
cm3.ChangeDutyCycle(6.7)
cm4.ChangeDutyCycle(6.7)
cm5.ChangeDutyCycle(6.7)
cm6.ChangeDutyCycle(6.7)
time.sleep(1)

start1 = time.time()
while (time.time()-start1) < 5:
    
    cm1.ChangeDutyCycle(7)
    cm2.ChangeDutyCycle(7)
    cm3.ChangeDutyCycle(7)
    cm4.ChangeDutyCycle(7)
    cm5.ChangeDutyCycle(7)
    cm6.ChangeDutyCycle(7)

    """
    throttle.neutral_position(cm1, 7)
    throttle.neutral_position(cm2, 11)
    throttle.neutral_position(cm3, 13)
    throttle.neutral_position(cm4, 15)
    """


while True:
    cm2.stop()
    cm4.stop()


cm1.stop()
cm2.stop()
cm3.stop()
cm4.stop()
print("stop()")
GPIO.cleanup()                                   
