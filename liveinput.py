from driver import Driver
from time import sleep
import RPi.GPIO as GPIO
from kbhit import KBHit

buggy = Driver([17,27,22,23])
try:
    kb = KBHit()

    print('Hit any key, or ESC to exit')
    while True:
        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 119: # ESC
                raise KeyboardInterrupt
            if c == "w":
                buggy.forward()
            elif c == "s":
                buggy.backward()
            elif c == "a":
                buggy.left()
            elif c == "d":
                buggy.right()
            else:
                buggy.stop()

    kb.set_normal_term()
except KeyboardInterrupt:
    buggy.kill()