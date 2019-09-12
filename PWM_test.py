#Coded by: Chad Martin
#Creation date: 25MAR2019
#Revision 1.0

#Purpose: to act as a proof of concept for using the PWM of the raspberry pi 
#			to control the speed of two diffrent motors given arguments of 
#			duty cycle of right wheel and ratio of right wheel to left Wheel

#Notes: there is some unexpected latency in the PWM for the right and left wheel
#		The latency seems to vary. At this point in time there is no problem with
#		this by there may be a problem in the future

import RPi.GPIO as GPIO
RW_PIN = 18;
LW_PIN = 13;
RW_ENA = 16;
LW_ENA = 11;
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RW_PIN,GPIO.OUT) # Right Wheel 
GPIO.setup(RW_ENA,GPIO.OUT) # Right Wheel 
GPIO.output(RW_ENA, 1)
GPIO.setup(LW_PIN,GPIO.OUT) # Left Wheel
GPIO.setup(LW_ENA,GPIO.OUT) # Left Wheel
GPIO.output(LW_ENA, 1)

r = GPIO.PWM(RW_PIN,50) # Arguments are pin and frequency
r.start(0) # Argument is initial duty cycle, it should be 0

l = GPIO.PWM(LW_PIN,50) # Arguments are pin and frequency
l.start(0) # Argument is initial duty cycle, it should be 0

ratio = 1 # Wheels will start off at the same ratio

while True:
	duty = input("\n\nSelect duty cycle in the range 0.0 to 100.0:") # Take duty cycle as input
	ratio = input("\nSelect a wheel ratio (Right/Left):") # Take ratio of right to left as input
	r.ChangeDutyCycle(duty) # Change duty cycle for right wheel
	l.ChangeDutyCycle((duty * ratio)) # Change duty cycle for left wheel with ratio

GPIO.cleanup()
