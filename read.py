import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader= SimpleMFRC522()

try:
    text=input("New Data")
    print("Place Your Id")
    reader.write(text)
    print("Registered")

finally:
    GPIO.cleanup()
