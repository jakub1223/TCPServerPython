import RPi.GPIO as GPIO
import time


def setup_GPIO():
    #GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    set_diode()


def blink_diode():
    make_blink()


def set_diode():
    GPIO.output(12, True)


def make_blink():
    LED = True
    i = 0
    while i < 10:
        GPIO.output(12, LED)
        time.sleep(0.5)
        LED = not LED
        i += 1

