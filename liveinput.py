from driver import Driver
from time import sleep
import RPi.GPIO as GPIO
import keyboard

try:
    buggy = Driver([17,27,22,23])
    while True:
        if keyboard.is_pressed('w'):
            buggy.forward()
        elif keyboard.is_pressed('s'):
            buggy.backward()
        elif keyboard.is_pressed('a'):
            buggy.left()
        elif keyboard.is_pressed('d'):
            buggy.right()
        else:
            buggy.stop()
except KeyboardInterrupt:
    GPIO.cleanup()