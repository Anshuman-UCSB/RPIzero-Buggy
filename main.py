from driver import Driver
from time import sleep
import RPi.GPIO as GPIO


try:
    buggy = Driver([17,27,22,23])

    buggy.forward()
    sleep(2)
    buggy.kill()
except KeyboardInterrupt:
    GPIO.cleanup()