import RPi.GPIO as IO  # calling for header file which helps us use GPIO’s of PI
import time  # calling for time to provide delays in program
import sys

IO.setwarnings(False)  # do not show any warnings
IO.setmode(IO.BCM)  # programming the GPIO by BCM pin numbers

# Initialize GPIO Pins as outputs
pins = [6, 22, 21, 20, 16, 12, 25, 24, 23, 18]
for pin in pins:
    IO.setup(pin, IO.OUT)

def send_a_command(command):  # execute the loop when “send_a_command” is called
    pin = command
    PORT(pin)  # calling 'PORT' to assign value to data port

    IO.output(6, 0)  # putting 0 in RS to tell LCD we are sending command
    IO.output(22, 1)  # telling LCD to receive command/data at the port by pulling EN pin high
    time.sleep(0.05)
    IO.output(22, 0)  # pulling down EN pin to tell LCD we have sent the data

    pin = 0
    PORT(pin)  # pulling down the port to stop transmitting

def send_a_character(character):  # execute the loop when “send_a_character” is called
    pin = character
    PORT(pin)

    IO.output(6, 1)
    IO.output(22, 1)
    time.sleep(0.05)
    IO.output(22, 0)

    pin = 0
    PORT(pin)

def PORT(pin):  # assigning PIN by taking PORT value
    if pin & 0x01 == 0x01:
        IO.output(21, 1)  # if bit0 of 8bit 'pin' is true, pull PIN21 high
    else:
        IO.output(21, 0)  # if bit0 of 8bit 'pin' is false, pull PIN21 low

    if pin & 0x02 == 0x02:
        IO.output(20, 1)
    else:
        IO.output(20, 0)

    if pin & 0x04 == 0x04:
        IO.output(16, 1)
    else:
        IO.output(16, 0)

    if pin & 0x08 == 0x08:
        IO.output(12, 1)
    else:
        IO.output(12, 0)

    if pin & 0x10 == 0x10:
        IO.output(25, 1)
    else:
        IO.output(25, 0)

    if pin & 0x20 == 0x20:
        IO.output(24, 1)
    else:
        IO.output(24, 0)

    if pin & 0x40 == 0x40:
        IO.output(23, 1)
    else:
        IO.output(23, 0)

    if pin & 0x80 == 0x80:
        IO.output(18, 1)  # if bit7 of 8bit 'pin' is true, pull PIN18 high
    else:
        IO.output(18, 0)  # if bit7 of 8bit 'pin' is false, pull PIN18 low

while True:
    send_a_command(0x01)  # sending 'all clear' command
    send_a_command(0x38)  # 16*2 line LCD
    send_a_command(0x0E)  # screen and cursor ON

    # Sending characters
    for char in "CIRCUITDIGEST":
        send_a_character(ord(char))  # Convert character to ASCII and send

    
