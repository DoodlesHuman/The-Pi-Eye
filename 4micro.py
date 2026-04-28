1	#Importing needed packages and libraries
2	import RPi.GPIO as GPIO
3	import time
4	import os
 	 
5	#Setting the GPIO Numbering and Logic
6	GPIO.setmode(GPIO.BOARD)
7	GPIO.setup(37, GPIO.IN, GPIO.PUD_UP)
 	 
8	#Running selected program
9	while True:
10	    input_state = GPIO.input(37)
11	    if input_state == False:
12	        print('Button 4 is Pressed')
13	        os.system('/home/pi/Micro.py')
14	        time.sleep(0.2)
