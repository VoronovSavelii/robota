import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
check = 6
state = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(check, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(check))
    #GPIO.output(led, (1 - GPIO.input(check)))
    time.sleep(0.2)