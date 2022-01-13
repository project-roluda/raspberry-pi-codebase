import RPi.GPIO as GPIO
import time


def throttle(motor):
    """Throttle motor to ensure movement"""    

    motor.start(0)
    GPIO.output(7, True)
    motor.ChangeDutyCycle(1)
    time.sleep(1)
    motor.ChangeDutyCycle(2)
    time.sleep(1)
    motor.stop()
