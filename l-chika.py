import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

for i in range(0, 10):
    GPIO.output(4, 1)
    time.sleep(1)
    GPIO.output(4,0)
    time.sleep(1)


GPIO.cleanup()

