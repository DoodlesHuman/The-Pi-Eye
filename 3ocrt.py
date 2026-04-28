#Importing needed packages and libraries
import RPi.GPIO as GPIO
import time
import os
 
#Setting the GPIO Numbering and Logic
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.IN, GPIO.PUD_UP)
 
#Running selected program
while True:
    input_state = GPIO.input(35)
    if input_state == False:
        print('Button 3 is Pressed')
        os.system('/home/pi/OCRO.py')
        time.sleep(0.2)
