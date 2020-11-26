import RPi.GPIO as GPIO


class Driver():
    
    def __init__(pins):
        #Right motor: pins[0]
        #Right back : pins[1]
        #Left motor: pins[2]
        #Left back : pins[3]
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins[0], GPIO.OUT)
        GPIO.setup(pins[1], GPIO.OUT)
        GPIO.setup(pins[2], GPIO.OUT)
        GPIO.setup(pins[3], GPIO.OUT)

    def forwards():
        GPIO.output(pins[0],0)
        GPIO.output(pins[1],1) 
        GPIO.output(pins[2],0) 
        GPIO.output(pins[3],1)
        
    def backwards():
        GPIO.output(pins[0],1)
        GPIO.output(pins[1],0) 
        GPIO.output(pins[2],1) 
        GPIO.output(pins[3],0)
    
    def left():
        GPIO.output(pins[0],1)
        GPIO.output(pins[1],0) 
        GPIO.output(pins[2],0) 
        GPIO.output(pins[3],1)
    
    def right():
        GPIO.output(pins[0],0)
        GPIO.output(pins[1],1) 
        GPIO.output(pins[2],1) 
        GPIO.output(pins[3],0)
        
    def stop():
        GPIO.output(pins[0],0)
        GPIO.output(pins[1],0) 
        GPIO.output(pins[2],0) 
        GPIO.output(pins[3],0)
        
    def kill():
        stop()
        GPIO.cleanup()
    