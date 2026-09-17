import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
up = 9
down = 10

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

GPIO.output(leds, 0)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(up):
        if (num < 255):
            num = num + 1
        print(num, dec2bin(num))
        time.sleep(0.2)

    if GPIO.input(down):
        if (num > 0):
            num = num - 1
        print(num, dec2bin(num))
        time.sleep(0.2)
    GPIO.output(leds, dec2bin(num))