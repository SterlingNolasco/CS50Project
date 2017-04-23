import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#moving forward 1.5 seconds
GPIO.setup(17,True)
GPIO.setup(18,False)
GPIO.setup(22,True)
GPIO.setup(23,False)
time.sleep(0.5)

#turning left 0.8 seconds
GPIO.setup(17,True)
GPIO.setup(18,False)
GPIO.setup(22,False)
GPIO.setup(23,False)
time.sleep(0.7)

#forward 1.5 seconds
GPIO.setup(22,True)
time.sleep(0.5)

#stops
GPIO.setup(17,False)
GPIO.setup(22,False)

