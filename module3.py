##############################################
# File Name: module3.py
# Version: 1.0
# Team No.: 26
# Team Name:
# Date: 28 Oct 15
##############################################

import RPi.GPIO as GPIO
import time
import sys, tty, termios

print '\nHi, I am PiBot, your very own learning robot..\n'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

ledOnTime=7
# Turn on LED
print 'Turn the LED on'
GPIO.output(8, True)
time.sleep(7)
print 'Turn the LED off'
GPIO.output(2, False)

GPIO.cleanup(8)
   
print "\nstop of program"
