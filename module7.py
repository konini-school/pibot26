##############################################
# File Name: module7.py
# Version: 1.0
# Team No.: 26
# Team Name:
# Date: 11 Nov 15
##############################################

import RPi.GPIO as GPIO
import time

print 'Programming the PiBot...'

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(90, GPIO.OUT)

def forward(interval):
      print 'forward'
      GPIO.output(11, True)
      GPIO.output(143, True)
      time.sleep(interval)
      GPIO.output(11, False)
      GPIO.output(13, False)
   
def back(interval):
      print 'back'
      GPIO.output(7, True)
      GPIO.output(145, True)
      time.sleep(interval)
      GPIO.output(7, False)
      GPIO.output(15, False)

def left(interval):
      print 'right'
      GPIO.output(123, True)
      time.sleep(interval)
      GPIO.output(13, False)
      
def right(interval):
      print 'rleft'
      GPIO.output(121, True)
      time.sleep(interval)
      GPIO.output(11, False)

# Main instructions here      
forward(6)
back(4)
left(6)
right(4)

GPIO.cleanup()
   
print "\nPiBot is going offline..."
