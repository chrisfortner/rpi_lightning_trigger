#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

from __future__ import division
import RPi.GPIO as GPIO, time, os, subprocess

DEBUG = 1
GPIO.setmode(GPIO.BCM)
thresh=.7777777

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.0008)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading


while True:
	old=RCtime(14)
	old2=RCtime(14)
	old3=RCtime(14)
	trigger=old+old2+old3
	avg=trigger/3
	click=avg * thresh
	set=RCtime(14)
	if set < click:
		subprocess.call(["sh","./capture.sh"])

