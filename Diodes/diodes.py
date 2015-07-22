import RPi.GPIO as GPIO
import time


def setup_GPIO():
    print('set')
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.OUT)


def blink_diode():
    set_diode()
    make_blink()


def set_diode():
    #GPIO.output(18, True)
    print('Diode 18 on')


def make_blink():
    print('blink')
    #LED = True
    #i = 0
    #while i < 10:
    #    GPIO.output(18, LED)
    #    time.sleep(0.5)
    #    LED = not LED
    #    i += 1

