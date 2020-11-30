import RPi.GPIO as GPIO
from time import *

pins = [17,27,22,23]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins [2], GPIO.OUT)
GPIO.setup(pins[3], GPIO.OUT)

stages = [
[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1],
[1,0,0,1]
]

delay = 0.0008

start = time()
stage = 0
print("starting drive")
while(time()-start < 5):
    state = stages[stage%len(stages)]
    GPIO.output(pins[0],state[0])
    GPIO.output(pins[1],state[1]) 
    GPIO.output(pins[2],state[2]) 
    GPIO.output(pins[3],state[3])
    sleep(delay)
    stage+=1

print("Finishing drive")
GPIO.cleanup()
