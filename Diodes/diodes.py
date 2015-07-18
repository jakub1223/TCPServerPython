__author__ = 'gonczor'


import RPi.GPIO as GPIO
import time


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)


def blink_diode(message):
    if message == "Hello world!":
        GPIO.output(18, True)
    else:
        make_blink()


def make_blink():
    LED = True
    i = 0
    while i < 10:
        GPIO.output(18, LED)
        time.sleep(0.5)
        LED = not LED
        i += 1