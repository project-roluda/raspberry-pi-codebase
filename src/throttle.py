import RPi.GPIO as GPIO
import time

def rotateAngle(motor, angle):
    duty = angle/18+3
    GPIO.output(7, True)
    motor.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(7, False)
    motor.ChangeDutyCycle(duty)


def throttle(motor, angle=20):
    """Throttle motor to ensure movement"""    

    motor.start(0)
    GPIO.output(7, True)
    motor.ChangeDutyCycle(1)
    time.sleep(1)
    #motor.ChangeDutyCycle(2)
    #time.sleep(1)
    motor.stop()

def neutral_position(motor, pin_number):
    motor.start(0)
    GPIO.output(11, True)
    motor.ChangeDutyCycle(7)
    time.sleep(1)
    