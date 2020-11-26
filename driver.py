import RPi.GPIO as GPIO


class Driver():
    
    def __init__(self, pins):
        #Right motor: pins[0]
        #Right back : pins[1]
        #Left motor: pins[2]
        #Left back : pins[3]
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pins[0], GPIO.OUT)
        GPIO.setup(self.pins[1], GPIO.OUT)
        GPIO.setup(self.pins[2], GPIO.OUT)
        GPIO.setup(self.pins[3], GPIO.OUT)

    def forwards(self):
        GPIO.output(self.pins[0],0)
        GPIO.output(self.pins[1],1) 
        GPIO.output(self.pins[2],0) 
        GPIO.output(self.pins[3],1)
        
    def backwards(self):
        GPIO.output(self.pins[0],1)
        GPIO.output(self.pins[1],0) 
        GPIO.output(self.pins[2],1) 
        GPIO.output(self.pins[3],0)
    
    def left(self):
        GPIO.output(self.pins[0],1)
        GPIO.output(self.pins[1],0) 
        GPIO.output(self.pins[2],0) 
        GPIO.output(self.pins[3],1)
    
    def right(self):
        GPIO.output(self.pins[0],0)
        GPIO.output(self.pins[1],1) 
        GPIO.output(self.pins[2],1) 
        GPIO.output(self.pins[3],0)
        
    def stop(self):
        GPIO.output(self.pins[0],0)
        GPIO.output(self.pins[1],0) 
        GPIO.output(self.pins[2],0) 
        GPIO.output(self.pins[3],0)
        
    def kill(self):
        stop()
        GPIO.cleanup()
    