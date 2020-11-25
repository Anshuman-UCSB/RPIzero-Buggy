import RPi.GPIO as GPIO
import sys
import keyboard


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)



try:
    while True:
        if sys.argv[1] == 'f':
            GPIO.output(17,1)
            GPIO.output(27,0) 
            GPIO.output(22,1) 
            GPIO.output(23,0)
        elif sys.argv[1] == 'b':
            GPIO.output(17,0)
            GPIO.output(27,1) 
            GPIO.output(22,0) 
            GPIO.output(23,1)
        elif sys.argv[1] == 'r':
            GPIO.output(17,0)
            GPIO.output(27,1) 
            GPIO.output(22,1) 
            GPIO.output(23,0)
        elif sys.argv[1] == 'l':
            GPIO.output(17,1)
            GPIO.output(27,0) 
            GPIO.output(22,0) 
            GPIO.output(23,1)

except KeyboardInterrupt:
    GPIO.cleanup()
