from driver import Driver
from keyboardMonitor import Keyboard
from time import sleep
import RPi.GPIO as GPIO


try:
    buggy = Driver([17,27,22,23])
    kb = Keyboard()
    while kb.live:
        if kb.isPressed('w'):
            buggy.forward()
        elif kb.isPressed('s'):
            buggy.backward()
        elif kb.isPressed('a'):
            buggy.left()
        elif kb.isPressed('d'):
            buggy.right()
        else:
            buggy.stop()
    buggy.kill()
except KeyboardInterrupt:
    GPIO.cleanup()