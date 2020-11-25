from driver import Driver
from time import sleep

buggy = Driver([17,27,22,23])

input("ready to drive?\n")
buggy.forward()
sleep(2)
buggy.kill()