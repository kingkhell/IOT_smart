import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcd_RS = 12
lcd_E = 7
lcd_D4= 8
lcd_D5= 25
lcd_D6 = 24
lcd_D7 = 23

lcd = LCD.Adafruit_CharLCD(lcd_RS, lcd_E, lcd_D4, lcd_D5, lcd_D6, lcd_D6, 0, 16, 2)

lcd.message("Hellow World")
